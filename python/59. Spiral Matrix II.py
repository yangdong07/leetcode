

# 59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        A = [[0] * n for _ in range(n)]
        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        i = 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                A[r][c] = i
                i += 1
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return A

def print_solution(A):
    for row in A:
        print(row)

print_solution(Solution().generateMatrix(3))