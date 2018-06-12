

# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[-1][-1] = True   # "" match ""

        # s = ""
        for j in range(m - 1, -1, -1):
            if p[j] == '*':
                dp[-1][j] = True
            else:
                break
        #
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if p[j] == '*':
                    dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j + 1] and (p[j] == s[i] or p[j] == '?')

        # print(' \t')
        # for j in range(len(p) + 1):
        #     print(p[j:], end='\t')
        # print()
        # for i in range(len(s) + 1):
        #     print(s[i:], end='\t')
        #     for j in range(len(p) + 1):
        #         print(dp[i][j], end='\t')
        #     print()

        return dp[0][0]


class Solution2:
    def isMatch(self, s, p):
        i = j = 0
        n = len(s)
        m = len(p)
        star = -1

        while i < n:
            if j < m and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < m and p[j] == '*':
                star = j        # remember the pos of *
                ii = i          # remember the pos of * match, first think it match ""
                j = star + 1    #   to  next pos
            elif star != -1:
                # if the normal match failed,
                # and there is star, ii += 1,
                # then re-search from (ii, star + 1)
                ii += 1
                i = ii
                j = star + 1
            else:
                # if no star and there is a failed match, return False
                return False
        while j < m and p[j] == '*':
            j += 1

        return j == m

print(Solution2().isMatch("abcd", '*'))
print(Solution2().isMatch("adceb", "*a*b"))
print(Solution2().isMatch("acdcb", "a*c?b"))
