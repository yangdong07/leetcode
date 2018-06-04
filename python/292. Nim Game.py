

# 292. Nim Game
# https://leetcode.com/problems/nim-game

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return 0 != n % 4