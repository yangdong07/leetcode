

# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # counter t
        counter = dict()
        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        missing = len(t)

        i = ii = 0
        l = len(s) + 1

        # move j, find missing
        for j, c in enumerate(s, 1):
            if c in counter:
                if counter[c] > 0:
                    missing -= 1
                counter[c] -= 1
            # move i, pop the beginning, make missing
            while not missing and i < j:
                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] > 0:
                        missing = 1   # break
                        if j - i < l:
                            l = j - i
                            ii = i
                i += 1
        return s[ii:ii+l] if l <= len(s) else ""

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABCX"))
print(Solution().minWindow("A", "A"))