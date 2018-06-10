

# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return "0"

        ans = [0] * (len(num1) + len(num2))

        for j, b in enumerate(num1):
            b = ord(b) - 48
            for i, a in enumerate(num2):
                a = ord(a) - 48
                ans[i + j + 1] += a * b

        for i in range(len(ans) - 1, 0, -1):
            ans[i-1], ans[i] = ans[i-1] + ans[i] // 10, chr(ans[i] % 10 + 48)

        ans[0] = '' if ans[0] == 0 else chr(ans[0] + 48)
        return ''.join(ans)


class Solution2:
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))


print(Solution2().multiply("123", "456"))
