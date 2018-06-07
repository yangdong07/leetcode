

# 39. Combination Sum
# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []

        def dfs(index, path, t):
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num == t:
                    results.append(path + [num])
                elif num < t:
                    dfs(i, path + [num], t - num)
                else:
                    return

        dfs(0, [], target)

        return results


print(Solution().combinationSum([2,3,6,7], 7))