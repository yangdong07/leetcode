

# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if nums[j] != nums[i] or nums[i] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
        return i + 1

class Solution2:
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        ans = nums[:2]
        for j in range(2, len(nums)):
            if nums[j] != ans[-1] or ans[-1] != ans[-2]:
                ans.append(nums[j])
        return len(ans)

def solve(nums):
    l = Solution2().removeDuplicates(nums)
    print(nums[:l])

solve([1,1,1,2,2,3])
solve([0,0,1,1,1,1,2,3,3])
solve([1,1,1,2,2,3])
