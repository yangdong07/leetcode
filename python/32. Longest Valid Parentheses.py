# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        maxlen = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i > dp[i-1] and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]
            print(i, dp[i], s[i], s[i-1-dp[i-1]])
            maxlen = max(maxlen, dp[i])

        return maxlen

# Solution().longestValidParentheses(')()())')
assert Solution().longestValidParentheses("(()))())(") == 4
