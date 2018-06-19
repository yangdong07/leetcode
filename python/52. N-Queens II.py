

# 52. N-Queens II
# https://leetcode.com/problems/n-queens-ii
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0

        def dfs(queens, slash, backslash):
            nonlocal ans
            j = len(queens)
            if n == j:
                ans += 1
                return

            for c in range(n):  # for each column
                if c not in queens and c + j not in slash and c - j not in backslash:
                    dfs(queens + [c], slash + [c + j], backslash + [c - j])

        dfs([], [], [])
        return ans


class Solution2:
    def totalNQueens(self, n):
        ans = 0

        def dfs(queens, slash, backslash):
            nonlocal ans
            j = len(queens)
            if n == j:
                ans += 1
                return

            for c in range(n):  # for each column
                if c not in queens and c + j not in slash and c - j not in backslash:
                    dfs(queens.union({c}), slash.union({c + j}), backslash.union({c - j}))

        dfs(set(), set(), set())
        return ans

for i in range(5):
    print(Solution2().totalNQueens(i))