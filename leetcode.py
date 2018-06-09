
import os
import sys
import shutil
import traceback
import time
import warnings

import argparse

import urllib.parse

from collections import defaultdict, OrderedDict
from pprint import pprint
from urllib.parse import urljoin

from git import Repo
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from pymongo import MongoClient

from html2markdown import html2markdown

labels = {
    'Easy': '💚',
    'Medium': '🧡',
    'Hard': '❤️',
}


def init_db():
    client = MongoClient('localhost', 27017)
    client.spider.drop_collection('leetcode')
    client.spider.create_collection('leetcode')
    leetcode = client.spider.leetcode
    leetcode.create_index("index", unique=True)
    return leetcode


def get_db(collection='leetcode'):
    client = MongoClient('localhost', 27017)
    return client.spider[collection]


def init_web_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome('/Users/yangdong/tools/chromedriver', chrome_options=chrome_options)
    return driver


# parse all problems page
def parse_page(page_content, collection):

    soup = BeautifulSoup(page_content, 'html.parser')
    table_body = soup.select_one('tbody.reactable-data')

    rows = table_body.find_all('tr')

    count = 0
    for row in rows:
        try:
            cols = row.find_all('td')
            index = cols[1].text.strip()
            title_link = cols[2].find('a')
            title = title_link.text.strip()

            locked = True if cols[2].select('i.fa-lock') else False

            problem_link = urljoin('https://leetcode.com/', title_link['href'])
            solution_link = cols[3].find('a')
            if solution_link:
                solution_link = urljoin('https://leetcode.com/problemset/all/', solution_link.get('href'))
            label = cols[5].text.strip()

            count = count + 1
            print(count, index, title)
            problem = dict(
                raw=str(row),
                index=index,
                title=title,
                problem_link=problem_link,
                solution_link=solution_link or '',
                label=label,
                locked=locked,
            )
            collection.update_one({'index': index}, {'$set': problem}, upsert=True)

        except:
            print('Error parse: ', str(row))
            traceback.print_exc()


# parse topic page
def parse_topic_page(page_content):

    soup = BeautifulSoup(page_content, 'html.parser')
    table_body = soup.select_one('tbody.reactable-data')

    rows = table_body.find_all('tr')

    problems = list()
    for row in rows:
        try:
            cols = row.find_all('td')
            index = cols[1].text.strip()
            problems.append(index)
        except:
            pass
    return problems


# get all problems
def init_all_problems():
    driver = init_web_driver()

    driver.get("https://leetcode.com/problemset/all/")
    time.sleep(5)
    # parse_page(driver.page_source)

    # show all problems
    for select in driver.find_elements_by_css_selector('select.form-control'):
        for option in select.find_elements_by_tag_name('option'):
            if option.text == 'all':
                option.click()

    leetcode = get_db()
    parse_page(driver.page_source, leetcode)


def show_problems(indices):
    leetcode = get_db()
    for problem in leetcode.find({'index': {'$in': indices}}):
        pprint(problem)


def update_topics():
    driver = init_web_driver()
    driver.get("https://leetcode.com/problemset/all/")
    time.sleep(5)

    # expand topic
    driver.find_element_by_css_selector('#expand-topic > div.btn').click()
    topic_links = driver.find_element_by_css_selector('#current-topic-tags').find_elements_by_tag_name('a')

    # get all topic link
    topic_link_dict = dict()
    for topic_link in topic_links:
        link = topic_link.get_attribute('href')
        topic = topic_link.find_element_by_css_selector('span.text-sm').text
        topic_link_dict[link] = topic

    # get url and parse topics
    problem_topics = dict()
    for link, topic in topic_link_dict.items():
        driver.get(link)
        time.sleep(1)

        problems = parse_topic_page(driver.page_source)

        for index in problems:
            if index not in problem_topics:
                problem_topics[index] = set()
            problem_topics[index].add(topic)

    pprint(problem_topics)

    leetcode = get_db()
    for index, topics in problem_topics.items():
        leetcode.update_one({'index': index}, {'$set': {'tags': list(topics)}})

    return problem_topics


def update_detail(indices):

    driver = init_web_driver()
    leetcode = get_db()

    for index in indices:
        problem = leetcode.find_one({'index': index})
        if not problem:
            continue
        print('update index: ', index)
        problem_link = problem['problem_link']
        driver.get(problem_link)
        driver.implicitly_wait(10)
        try:
            content = driver.find_elements_by_css_selector('div.question-content > div')[1].get_attribute('innerHTML')
            leetcode.update_one({'index': problem['index']}, {'$set': {'description': content, 'status': 'ok'}})
        except:
            leetcode.update_one({'index': problem['index']}, {'$set': {'status': 'error'}})

    driver.close()


def search_solutions_and_codes(path='./solutions'):
    # search solutions
    solutions = {}
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.md'):
            index = file_name.split('.')[0]
            solutions[index] = file_path

    # search code
    code_candidates = {'python': '.py'}
    code_links = defaultdict(dict)
    for code, suffix in code_candidates.items():
        code_path = './' + code
        if os.path.exists(code_path):
            for file_name in os.listdir(code_path):
                file_path = os.path.join(code_path, file_name)
                if os.path.isfile(file_path) and file_name.endswith(suffix):
                    index = file_name.split('.')[0]
                    code_links[index][code] = file_path
    return solutions, code_links


def get_tag_problems(problems):
    problems = {p['index']: p for p in problems}

    topics = defaultdict(list)
    for index, problem in problems.items():
        if 'tags' not in problem:
            topics['other'].append(problem)
        else:
            tags = problem['tags']
            for tag in tags:
                topics[tag].append(problem)

    tag_problems = OrderedDict()
    for tag in sorted(topics.keys()):
        tag_problems[tag] = topics[tag]
    return tag_problems


def generate_table(problems, solutions, code_links):
    # headers = ['', '#', 'Title', 'Tags', 'Difficulty', 'Article', 'Solution']
    headers = ['#', 'Title', 'Difficulty', 'Article', 'Solution', 'Code']
    markers = [':---:' for _ in headers]
    markers[1] = '---'   # Title
    headers = [''] + headers + ['']
    markers = [''] + markers + ['']

    table = list()
    table.append("|".join(headers))
    table.append("|".join(markers))

    for problem in problems:
        index = problem['index']
        locked = problem['locked']
        lock = '🔒' if locked else ''
        problem_link = '[%s](%s) %s' % (problem['title'], problem['problem_link'], lock)

        # problem_tags = ''
        # if 'tags' in problem and problem['tags']:
        #     problem_tags = ', '.join(problem['tags'])

        article_link = ''
        if 'solution_link' in problem and problem['solution_link']:
            article_link = '[💡](%s)' % problem['solution_link']

        solution_link = ''
        if index in solutions:
            solution_link = os.path.join('..', solutions[index])
            solution_link = '[📜](%s)' % urllib.parse.quote(solution_link)

        code_link = ''
        if index in code_links:
            code_link = ', '.join(['[%s](%s)' % (c, urllib.parse.quote(os.path.join('..', cl)))
                                   for c, cl in code_links[index].items()])
            print(code_link)
        content = [
            '',
            index,
            problem_link,
            # problem_tags,
            labels.get(problem['label'], '💔'),
            article_link,
            solution_link,
            code_link,
            '',
        ]
        table.append("|".join(content))

    return '\n'.join(table)


def generate_tables_by_tag():
    leetcode = get_db()
    tag_problems = get_tag_problems(leetcode.find())
    solutions, code_links = search_solutions_and_codes('./solutions')

    for topic in tag_problems:
        file_path = os.path.join('./topics', topic + '.md')
        with open(file_path, 'w') as f:
            f.write('\n## %s\n\n' % topic)
            f.write(generate_table(tag_problems[topic], solutions, code_links))


def generate_readme():
    leetcode = get_db()
    tag_problems = get_tag_problems(leetcode.find())
    solutions, _ = search_solutions_and_codes('./solutions')

    solved_count = defaultdict(int)
    for tag, problems in tag_problems.items():
        solved = [p for p in problems if p['index'] in solutions]
        solved_count[tag] = len(solved)

    headers = ['Topic', 'Total', 'Solved', 'Progress']
    markers = ['-'*len(h) for h in headers]
    markers[-1] = markers[-1] + ':'
    headers = [''] + headers + ['']
    markers = [''] + markers + ['']

    table = list()
    table.append("|".join(headers))
    table.append("|".join(markers))

    # tag tables
    for tag in tag_problems:
        tag_link = urllib.parse.quote(os.path.join('./topics', tag + '.md'))
        count = len(tag_problems[tag])
        # print
        solved = solved_count[tag]
        progress = 100.0 * solved / count
        content = [
            '',
            '[%s](%s)' % (tag, tag_link),
            str(count),
            # problem_tags,
            str(solved),
            '%5.2f %%' % progress,
            '',
        ]
        table.append('|'.join(content))

    total = leetcode.find().count()
    solved = len(solutions.keys())
    content = [
        '',
        'Total',
        str(total),
        # problem_tags,
        str(solved),
        '%.2f %%' % (100.0 * solved / total),
        '',
    ]
    table.append('|'.join(content))

    with open('README.md', 'w') as f:
        f.write('\n## LeetCode\n\n')
        f.write('\n'.join(table))


def generate_solution_template(index):
    leetcode = get_db()
    problem = leetcode.find_one({'index': index})
    if not problem:
        raise Exception('problem %s not found' % index)

    title = '%s. %s' % (index, problem['title'])
    md_file = title + '.md'
    py_file = title + '.py'

    if os.path.exists(md_file):
        warnings.warn('Be careful!!! Overwriting %s' % md_file)
        time.sleep(1)

    # TODO: maybe unlock someday, if i'm rich.
    locked = problem.get('locked')
    if locked:
        raise Warning('The Problem "%s. %s" is Locked, You should subscribe to unlock' % (index, problem['title']))

    description = problem.get('description')

    if not description:
        warnings.warn('No Description here, need fetch from leetcode')
        update_detail([index])

        # re get the problem
        problem = leetcode.find_one({'index': index})
        if not problem:
            raise Exception('problem %s not found' % index)
        if problem['status'] != 'ok':
            pprint(problem)
            raise Exception('problem %s is not ok' % index)
        if not problem.get('description'):
            raise Exception('no description here, please check it: %s' % problem['problem_link'])

    abstract = ''
    topics = problem.get('tags')
    if topics:
        abstract = ', '.join(map(lambda x: '**' + x + '**', topics)) + '    '

    label = labels.get(problem['label'], '💔')
    abstract += '[%s](%s)' % (label, problem['problem_link']) + '    '
    if problem.get('solution_link'):
        abstract += '\t[💡](%s)' % problem['solution_link']

    # be careful here, be careful about the relative path
    code_link = '[Code](../python/%s)' % urllib.parse.quote(py_file)

    markdown = html2markdown(problem['description'])

    with open(md_file, 'w') as f:
        f.write('### %s\n\n' % md_file[:-3])
        # write topics
        f.write('%s\n\n' % abstract)
        f.write('#### Description\n\n')
        f.write(markdown)
        f.write('\n\n#### Analysis\n\n')
        f.write('#### %s\n\n' % code_link)

    # generate python empty file
    if not os.path.exists(py_file):
        with open(py_file, 'w') as f:
            f.write('\n\n# %s\n' % py_file[:-3])
            f.write('# %s\n\n' % problem['problem_link'])


def solved_and_commit(index):
    leetcode = get_db()
    problem = leetcode.find_one({'index': index})
    if not problem:
        raise Exception('problem %s not found' % index)

    title = '%s. %s' % (index, problem['title'])
    files = [title + '.md', title + '.py']

    # move files
    to_move = {}
    path_map = {'py': 'python', 'md': 'solutions'}
    for f in files:
        if not os.path.exists(f):
            warnings.warn('solution file <%s> not exists' % f)
            continue

        suffix = f.rsplit('.', 1)[-1]
        if suffix in path_map:
            path = os.path.join(path_map[suffix], f)
            to_move[f] = path
        else:
            warnings.warn('<%s> stay here' % f)

    print('Plan to Move:\n')
    for src, dst in to_move.items():
        print('\t %s ---> %s' % (src, dst))
    input('\nReady to Move?')

    for src, dst in to_move.items():
        shutil.move(src, dst)

    # udpate readme and tables
    generate_readme()
    generate_tables_by_tag()

    # git commit and push
    git = Repo('.').git
    print(git.add('.'))
    print(git.status())

    default_summary = '%s, Solved' % title
    commit = input('\nCheck git status, and Input Summary: [%s]\n' % default_summary)
    commit = commit or default_summary
    print(git.commit('-m', commit))

    input('Ready to Push?')
    print(git.push())


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    parser_init = subparsers.add_parser('init', help='init db and init all problems')
    parser_update = subparsers.add_parser('update', help='update tags or details')
    parser_generate = subparsers.add_parser('generate', help='generate readme or solution template')

    options_init = parser_init.add_mutually_exclusive_group()
    options_init.add_argument('--db', action='store_true')
    options_init.add_argument('-p', '--problems', action='store_true')
    options_init.add_argument('-i', '--index', nargs='+')

    options_update = parser_update.add_mutually_exclusive_group()
    options_update.add_argument('--tags', action='store_true')
    options_update.add_argument('--index', nargs='+')

    options_generate = parser_generate.add_mutually_exclusive_group()
    options_generate.add_argument('--readme', action='store_true')
    options_generate.add_argument('--tables', action='store_true')
    options_generate.add_argument('--index', nargs=1)
    options_generate.add_argument('--solved', nargs=1)

    args = parser.parse_args()

    # print(args)
    if args.command == 'init':
        if args.db:
            print('init database')
            init_db()
        elif args.problems:
            print('init problems')
            init_all_problems()
        elif args.index:
            show_problems(args.index)
        else:
            parser_init.print_help()
    elif args.command == 'update':
        if args.tags:
            update_topics()
        elif args.index:
            update_detail(args.index)
        else:
            parser_update.print_help()
    elif args.command == 'generate':
        if args.readme:
            generate_readme()
        elif args.tables:
            generate_tables_by_tag()
        elif args.index:
            generate_solution_template(args.index[0])
        elif args.solved:
            solved_and_commit(args.solved[0])
        else:
            parser_generate.print_help()
    else:
        parser.print_help()
