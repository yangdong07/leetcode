

# 89. Gray Code
# https://leetcode.com/problems/gray-code

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        code = [0]
        for i in range(n):
            b = 1 << i
            code.extend((c + b for c in reversed(code)))
        return code

print(Solution().grayCode(4))