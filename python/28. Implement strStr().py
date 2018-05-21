

# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            j = i
            k = 0
            while k < len(needle) and haystack[j] == needle[k]:
                j += 1
                k += 1
            if k == len(needle):
                return i
        return -1

print(Solution().strStr("hello", "ll"))
