

# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1, p2 = 0, 1
        for i in range(n):
            p1, p2 = p2, p1 + p2

        return p2