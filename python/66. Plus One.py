

# 66. Plus One
# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        if not digits:
            return [1]

        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)

        if carry:
            return [1] + digits
        else:
            return digits