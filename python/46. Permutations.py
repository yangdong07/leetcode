

# 46. Permutations
# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]


class Solution2:
    def permute(self, nums):
        permutations = [[]]
        for num in nums:
            permutations = [p[:i] + [num] + p[i:] for p in permutations for i in range(len(p) + 1)]
        return permutations

from pprint import pprint
pprint(Solution2().permute([1, 2, 3]))