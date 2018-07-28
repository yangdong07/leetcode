

# 90. Subsets II
# https://leetcode.com/problems/subsets-ii

import collections

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n, c in collections.Counter(nums).items():
            l = len(ans)
            for i in range(1, c + 1):
                for j in range(l):
                    ans.append(ans[j] + [n] * i)
        return ans


class Solution2:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]

        c = 0
        nums.append('x')  # end sentinal
        for i in range(len(nums) - 1):
            c += 1
            if nums[i] != nums[i + 1]:
                l = len(ans)
                n = nums[i]
                for cc in range(1, c + 1):
                    for j in range(l):
                        ans.append(ans[j] + [n] * cc)
                c = 0
        return ans


print(Solution2().subsetsWithDup([1,2,2]))

