

# 68. Text Justification
# https://leetcode.com/problems/text-justification


class Solution:
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type max_width: int
        :rtype: List[str]
        """
        ans = []
        line = []
        letters = 0
        for word in words:
            if letters + len(line) + len(word) > max_width:
                slots = len(line) - 1 or 1
                for i in range(max_width - letters):
                    line[i % slots] += ' '
                ans.append(''.join(line))
                line, letters = [], 0
            line.append(word)
            letters += len(word)

        ans.append(' '.join(line).ljust(max_width))
        return ans


def print_solution(*args):
    for line in Solution().fullJustify(*args):
        print(line)


print_solution(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20)

print_solution(["What","must","be","acknowledgment","shall","be"], 16)

print_solution(["This", "is", "an", "example", "of", "text", "justification."], 16)