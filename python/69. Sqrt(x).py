

# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x

        while l < r:
            mid = (l + r + 1) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l


class Newton:
    def mySqrt(self, x):
        s = x
        while s * s > x:
            s = (s + x // s) // 2
        return s

Solution = Newton

print(Solution().mySqrt(0))
print(Solution().mySqrt(1))
print(Solution().mySqrt(8))
print(Solution().mySqrt(9))
print(Solution().mySqrt(15))
print(Solution().mySqrt(16))