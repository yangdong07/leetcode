

# 38. Count and Say
# https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            pd, tmp, count = s[0], "", 0
            for d in s:
                if d == pd:
                    count += 1
                else:
                    tmp += str(count) + pd
                    pd = d
                    count = 1
            tmp += str(count) + pd
            s = tmp
        return s


for i in range(1, 10):
    print(Solution().countAndSay(i))