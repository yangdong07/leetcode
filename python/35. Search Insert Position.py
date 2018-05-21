

# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums)
        while i < j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        return i

assert Solution().searchInsert([1, 2, 3, 5], 5) == 3
assert Solution().searchInsert([1, 2, 3, 5], 1) == 0
assert Solution().searchInsert([1, 2, 3, 5], 2) == 1
assert Solution().searchInsert([1, 2, 3, 5], 4) == 3
assert Solution().searchInsert([1, 2, 3, 5], 7) == 4