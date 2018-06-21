

# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        ml, mr = 0, m - 1
        while ml < mr:
            mid = (ml + mr + 1) // 2
            if matrix[mid][0] > target:
                mr = mid - 1
            else:
                ml = mid

        nl, nr = 0, n - 1
        while nl < nr:
            mid = (nl + nr + 1) // 2
            if matrix[ml][mid] > target:
                nr = mid - 1
            else:
                nl = mid

        return matrix[ml][nl] == target


def solve(*args):
    print(Solution().searchMatrix(*args))


solve( [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 11)


