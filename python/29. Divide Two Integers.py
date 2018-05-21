

# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1
        if not positive:
            quotient = -quotient
        return min(max(-2147483648, quotient), 2147483647)

print(Solution().divide(100, 3))
