

# 47. Permutations II
# https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def dfs(rest):
            if len(rest) == 1:
                return [rest]

            seen = None
            permutations = []
            for i, n in enumerate(rest):
                if n != seen:
                    seen = n
                    permutations.extend([[n] + p for p in dfs(rest[:i] + rest[i+1:])])
            return permutations

        return dfs(nums)


class Solution2:
    def permuteUnique(self, nums):
        permutations = [[]]
        for num in nums:
            np = []
            for p in permutations:
                for i in range(len(p) + 1):
                    np.append(p[:i] + [num] + p[i:])
                    if i < len(p) and p[i] == num:
                        break
            permutations = np
        return permutations


print(Solution2().permuteUnique([1, 1, 2]))
print(Solution2().permuteUnique([1, 1, 2, 2]))