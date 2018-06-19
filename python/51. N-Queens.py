

# 51. N-Queens
# https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def is_valid(j, c, queens):
            for i, q in enumerate(queens):
                if c == q or c == q + j - i or c == q + i - j:
                    return False
            return True

        ans = []

        def dfs(queens):
            j = len(queens)
            if n == j:
                ans.append(queens)
                return

            for c in range(n):  # for each column
                if is_valid(j, c, queens):
                    dfs(queens + [c])
        dfs([])
        return [['.' * c + 'Q' + '.' * (n - c - 1) for c in s] for s in ans]

    def solveNQueens2(self, n):
        ans = []

        def dfs(queens, slash, backslash):
            j = len(queens)
            if n == j:
                ans.append(queens)
                return

            for c in range(n):  # for each column
                if c not in queens and c + j not in slash and c - j not in backslash:
                    dfs(queens + [c], slash + [c + j], backslash + [c - j])
        dfs([], [], [])
        return [['.' * c + 'Q' + '.' * (n - c - 1) for c in s] for s in ans]

print(Solution().solveNQueens2(4))