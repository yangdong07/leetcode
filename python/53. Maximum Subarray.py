

# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = s = nums[0]
        for n in nums[1:]:
            if s > 0:
                s += n
            else:
                s = n
            maxsum = max(s, maxsum)
        return maxsum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))