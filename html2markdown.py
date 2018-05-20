
import re
from html.parser import HTMLParser


class HTML2Markdown(HTMLParser):

    def __init__(self):
        super().__init__()
        self.text_list = list()
        self.ignore_mark = ''

    def convert(self, html):
        self.feed(html)
        self.close()
        return ''.join(self.text_list).strip()

    def handle_starttag(self, tag, attrs):
        if self.ignore_mark:
            return

        markdown_symbol = ''

        if tag == 'strong':
            markdown_symbol = '**'
        elif tag == 'em':
            markdown_symbol = '_'
        elif tag == 'pre':
            self.ignore_mark = tag
            markdown_symbol = '```\n'
        elif tag == 'code':
            markdown_symbol = '`'
        elif tag == 'sup':
            markdown_symbol = '^'
        # TODO: ul/li has some bugs, should use sub parser, solve this problem recursive
        elif tag == 'ul':
            markdown_symbol = ''
        elif tag == 'li':
            markdown_symbol = '- '

        self.text_list.append(markdown_symbol)

    def handle_endtag(self, tag):

        if self.ignore_mark and tag != self.ignore_mark:
            return

        self.ignore_mark = ''
        markdown_symbol = ''
        if tag == 'strong':
            markdown_symbol = '**'
        elif tag == 'em':
            markdown_symbol = '_'
        elif tag == 'pre':
            markdown_symbol = '```\n'
        elif tag == 'p':
            markdown_symbol = '\n'
        elif tag == 'code':
            markdown_symbol = '`'
        elif tag == 'li':
            markdown_symbol = ''
        self.text_list.append(markdown_symbol)

    def handle_data(self, data):
        self.text_list.append(data)


def beautify_markdown(text):
    """reduce empty lines, ie. \n{3,} --> \n\n"""
    text = re.sub(r'\n{3,}', r'\n\n', text)
    text = re.sub(r'([^\n])```', r'\1\n```', text)

    # TODO: fix ul/li bugs here
    text = re.sub(r'\n\s+-', '\n-', text)
    return text


def html2markdown(html):
    parser = HTML2Markdown()
    return beautify_markdown(parser.convert(html))


if __name__ == '__main__':
    text = html2markdown('''
<div><p>Given an array of integers, return <strong>indices</strong> of the two numbers such that they add up to a specific target.</p>
<p>You may assume that each input would have <strong><em>exactly</em></strong> one solution, and you may not use the <em>same</em> element twice.</p>
<p><strong>Example:</strong></p>
<pre>Given nums = [2, 7, 11, 15], target = 9,



Because nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9,
return [<strong>0</strong>, <strong>1</strong>].
</pre>
<p> </p>
</div>
    '''
    )

    print(text.strip())
