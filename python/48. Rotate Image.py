

# 48. Rotate Image
# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution2:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - n // 2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                    A[~j][i], A[~i][~j], A[j][~i], A[i][j]


class Solution3:
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])


A = [[1,2,3],[4,5,6],[7,8,9]]

Solution3().rotate(A)

print(A)