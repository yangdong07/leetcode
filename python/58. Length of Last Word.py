

# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length


class Solution2:
    def lengthOfLastWord(self, s):
        return len(s.rstrip().rsplit(' ', 1)[-1])

print(Solution().lengthOfLastWord("Hello World"))