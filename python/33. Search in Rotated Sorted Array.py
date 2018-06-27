

# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the min
        n = len(nums)
        if n == 0:
            return -1

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        i = lo
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[(mid + i) % n]:
                lo = mid + 1
            else:
                hi = mid
        i = (lo + i) % n
        return i if nums[i] == target else -1


class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo + 1] else -1


class Solution3:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return l if nums[l] == target else -1

Solution = Solution1
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))