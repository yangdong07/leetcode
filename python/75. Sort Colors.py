

# 75. Sort Colors
# https://leetcode.com/problems/sort-colors

class Solution1:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3

        for n in nums:
            counter[n] += 1

        color = 0
        for i in range(len(nums)):
            while not counter[color]:
                color += 1
            counter[color] -= 1
            nums[i] = color


class Solution2:
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = 0, nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = 2, nums[r]
                r -= 1
            else:
                i += 1

Solution = Solution2


def solve(*args):
    nums, = args
    Solution().sortColors(nums)
    print(nums)

solve([2,0,2,1,1,0])