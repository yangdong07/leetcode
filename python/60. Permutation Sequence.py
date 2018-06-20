

# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        nums = [i for i in range(n + 1)]
        factorial = 1
        factorials = [1]
        for i in range(1, n):
            factorial *= i
            factorials.append(factorial)

        k = k - 1
        for i in range(n - 1, -1, -1):
            j, k = divmod(k, factorials[i])
            ans.append(str(nums.pop(j + 1)))
        return ''.join(ans)

print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(9, 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1))