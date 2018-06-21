

# 72. Edit Distance
# https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        if m > n:
            n, m, word1, word2 = m, n, word2, word1
        if m == 0:
            return n

        dp = list(range(m + 1))
        for i in range(n):
            prev = i  # left up corner
            dp[0] = i + 1
            for j in range(m):
                cache = dp[j + 1]
                if word1[i] == word2[j]:
                    dp[j + 1] = prev
                else:
                    dp[j + 1] = min(prev, dp[j], cache) + 1
                prev = cache

        return dp[m]

# Solution().minDistance('abc', 'efg')
Solution().minDistance('a', 'a')

