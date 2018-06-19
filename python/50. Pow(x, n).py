

# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1.0
        if n < 0:
            x = 1.0 / x
            n = -n

        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n >>= 1

        return ans

    def myPow2(self, x, n):
        return x ** n

print(Solution().myPow2(2.000, 10))
print(Solution().myPow2(2.000, -2))