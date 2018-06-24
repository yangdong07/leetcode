

# 78. Subsets
# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            ans.extend([subset + [n] for subset in ans])
        return ans


class Solution2:
    def subsets(self, nums):

        def subset(i):
            if i == len(nums):
                return [[]]
            ss = subset(i + 1)
            ss.extend([s + [nums[i]] for s in ss])
            return ss

        return subset(0)


class Solution3:

    def subsets(self, nums):
        ans = []

        def dfs(s, path):
            # print(path)
            ans.append(path)
            for i in range(s, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return ans


print(Solution2().subsets([1, 2, 3]))