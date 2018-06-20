

# 67. Add Binary
# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a), len(b)

        if la > lb:
            la, lb, a, b = lb, la, b, a

        carry = 0
        ans = []
        for i in range(la):
            carry, s = divmod(int(a[~i]) + int(b[~i]) + carry, 2)
            ans.append(str(s))

        for i in range(la, lb):
            carry, s = divmod(int(b[~i]) + carry, 2)
            ans.append(str(s))

        if carry:
            ans.append('1')

        return ''.join(reversed(ans))


class Solution2:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

print(Solution2().addBinary("111", "1"))