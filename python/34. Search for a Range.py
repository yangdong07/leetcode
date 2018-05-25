

# 34. Search for a Range
# https://leetcode.com/problems/search-for-a-range

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(t):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < t:
                    l = m + 1
                else:
                    r = m
            return l

        l = binary_search(target)

        if len(nums) == l or nums[l] != target:
            return [-1, -1]

        return [l, binary_search(target + 1) - 1]


print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([1], 1))