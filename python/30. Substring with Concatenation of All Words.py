

# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s, words):
        result = []

        if not s or not words:
            return []

        n = len(s)
        l = len(words[0])
        m = l * len(words)

        d = dict()
        for word in words:
            d[word] = d[word] + 1 if word in d else 1

        for i in range(min(l, n - m + 1)):
            seen = dict()
            j = k = i   # j: 子串起始位置； k: 单词起始位置
            while j + m <= n:
                word = s[k:k+l]
                k += l
                if word not in d:
                    j = k
                    seen.clear()
                else:
                    seen[word] = seen[word] + 1 if word in seen else 1
                    while seen[word] > d[word]:
                        seen[s[j:j+l]] -= 1
                        j += l
                    if k - j == m:
                        result.append(j)

        return result


assert Solution().findSubstring("foobarthebarfoo", ["foo", "bar"]) == [0, 9]
