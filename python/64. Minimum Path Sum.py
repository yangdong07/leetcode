

# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum



class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = []
        s = 0
        for x in grid[0]:
            s += x
            dp.append(s)
        # print(dp)
        for i in range(1, len(grid)):
            dp[0] += grid[i][0]
            for j in range(1, len(dp)):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
            # print(dp)
        return dp[-1]

assert Solution().minPathSum([[1,3,1], [1, 5, 1], [4, 2, 1]]) == 7
