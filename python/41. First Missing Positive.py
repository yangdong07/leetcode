

# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] > len(nums) or nums[i] < 1 or nums[nums[i] - 1] == nums[i]:
                    nums[i] = 0
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        else:
            return len(nums) + 1


print(Solution().firstMissingPositive([1, 2, 0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))
print(Solution().firstMissingPositive([]))
print(Solution().firstMissingPositive([1]))   # 2
print(Solution().firstMissingPositive([4]))   # 2