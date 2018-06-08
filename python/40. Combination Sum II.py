

# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates, target):
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

                if i > index and num == candidates[i-1]:
                    continue

                if num == t:
                    results.append(path + [num])
                elif num < t:
                    dfs(i+1, path + [num], t - num)
                else:
                    return

        dfs(0, [], target)

        return results


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))