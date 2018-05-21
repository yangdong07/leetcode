

# 27. Remove Element
# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        return i

nums = [3, 2, 2, 3]
print(Solution().removeElement(nums, 2))
print(nums)
