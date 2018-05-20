

# 31. Next Permutation
# https://leetcode.com/problems/next-permutation


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # find first decrease value
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1

        # swap with the just bigger
        if i >= 0:
            j = i + 1
            while j < n:
                if j == n - 1 or nums[i] >= nums[j + 1]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j += 1

        # reverse
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


test_nums = [3, 8, 7, 2, 1]
Solution().nextPermutation(test_nums)
print(test_nums)

test_nums = [1, 5, 1]
Solution().nextPermutation(test_nums)
print(test_nums)  # [5, 1, 1]