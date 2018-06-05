

# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        zero = ord('0')
        valid = set(['.'] + [chr(zero + i) for i in range(1, 10)])

        def is_not_valid(seen, c):
            if c not in valid:
                return True
            if c != '.':
                if c in seen:
                    return True
                else:
                    seen.add(c)
            return False

        for i in range(9):
            row = set()
            column = set()
            box = set()
            for j in range(9):
                if is_not_valid(row, board[i][j]) or \
                   is_not_valid(column, board[j][i]) or \
                   is_not_valid(box, board[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3]):
                    return False
        return True


class Solution2:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in rows[i] or \
                       num in cols[j] or \
                       num in boxes[3 * (i // 3) + j // 3]:
                        return False
                    else:
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[3 * (i // 3) + j // 3].add(num)
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
assert Solution2().isValidSudoku(board)
