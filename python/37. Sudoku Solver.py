

# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # analysis
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if board != '.':
                    box_index = 3 * (i // 3) + (j // 3)
                    rows[i].add(digit)
                    cols[j].add(digit)
                    boxes[box_index].add(digit)

        # candidates
        candidates = list()
        all_digits = set("123456789")
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    box_index = 3 * (i // 3) + (j // 3)
                    rest = all_digits - rows[i] - cols[j] - boxes[box_index]
                    candidates.append(((i, j), rest, len(rest)))
        candidates.sort(key=lambda t: t[2])

        # solve
        depth = len(candidates)

        def solve(ci):
            if ci == depth:
                return True

            r, c = candidates[ci][0]
            digits = candidates[ci][1]
            bi = 3 * (r // 3) + (c // 3)

            for d in digits:
                if not (d in rows[r] or d in cols[c] or d in boxes[bi]):
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[bi].add(d)
                    if solve(ci+1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[bi].remove(d)

            return False

        solve(0)


sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Solution().solveSudoku(sudoku)

for row in sudoku:
    print(row)