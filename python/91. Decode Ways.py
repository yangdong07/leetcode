

# 91. Decode Ways
# https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [1, 1]   # "",  "d"

        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp.append(dp[-2])
                else:       # '00', '30', '40'... invalid
                    return 0
            elif 9 < int(s[i - 1: i + 1]) < 27:
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])

        return dp[-1]


class Solution2:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        d2, d1 = 1, 1
        d = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] not in {'1', '2'}: # '00', '30', '40'... invalid
                    return 0
                d = d2
            elif 9 < int(s[i - 1: i + 1]) < 27:
                d = d1 + d2
            else:
                d = d1

            d2, d1 = d1, d

        return d


Solution = Solution2

def expect(answer, *args):
    solution = Solution().numDecodings(*args)

    if solution == answer:
        print(*args, "pass", answer)
    else:
        print(*args, "fail", answer, solution)

expect(0, "0")
expect(0, "100")
expect(1, "101")
expect(3, "223")

#
# print(Solution().numDecodings("0"))    #
# print(Solution().numDecodings("100"))  # 0
# print(Solution().numDecodings("223"))
# print(Solution().numDecodings("223323231212343"))