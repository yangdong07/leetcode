

# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        r0 = c0 = False

        # mark first row and first col
        for i in range(m):
            if matrix[i][0] == 0:
                c0 = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                r0 = True
                break

        # mark 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # set 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # set first row and first col 0
        if r0:
            for j in range(n):
                matrix[0][j] = 0
        if c0:
            for i in range(m):
                matrix[i][0] = 0


def print_solution(*args):
    A, = args
    Solution().setZeroes(A)
    for row in A:
        print(row)

print_solution([[1,1,1],[1,0,1],[1,1,1]])
print_solution([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
print_solution([[1,0,3]])
