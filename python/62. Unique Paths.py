

# 62. Unique Paths
# https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        solutions = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                solutions[j] += solutions[j - 1]

        return solutions[-1]

print(Solution().uniquePaths(7, 3))