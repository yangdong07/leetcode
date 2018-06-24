

# 79. Word Search
# https://leetcode.com/problems/word-search
from collections import Counter

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        l = len(word)

        def search(r, c, i):
            if i == l - 1:
                return board[r][c] == word[i]
            if board[r][c] != word[i]:
                return False

            board[r][c] = '*'   # mask

            found = (r > 0 and search(r - 1, c, i + 1)) or \
                    (r < m - 1 and search(r + 1, c, i + 1)) or \
                    (c > 0 and search(r, c - 1, i + 1)) or \
                    (c < n - 1 and search(r, c + 1, i + 1))

            board[r][c] = word[i]  # unmask

            return found

        for x in range(m):
            for y in range(n):
                if search(x, y, 0):
                    return True
        return False


class Solution2:
    def exist(self, board, word):

        c_board = Counter([c for row in board for c in row])
        c_word = Counter(word)
        for c in c_word:
            if c not in c_board or c_board[c] < c_word[c]:
                return False

        m, n = len(board), len(board[0])
        l = len(word)
        def search(r, c, i):
            if i == l - 1:
                return board[r][c] == word[i]
            if board[r][c] != word[i]:
                return False

            board[r][c] = '*'   # mask

            found = (r > 0 and search(r - 1, c, i + 1)) or \
                    (r < m - 1 and search(r + 1, c, i + 1)) or \
                    (c > 0 and search(r, c - 1, i + 1)) or \
                    (c < n - 1 and search(r, c + 1, i + 1))

            board[r][c] = word[i]  # unmask

            return found

        for x in range(m):
            for y in range(n):
                if search(x, y, 0):
                    return True
        return False


print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(Solution().exist([["A"]], "A"))