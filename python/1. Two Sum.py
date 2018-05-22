

# 1. Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

Solution().twoSum([2, 7, 11, 15], 9)
