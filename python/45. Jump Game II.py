

# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = [len(nums)] * len(nums)
        jumps[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                jumps[j] = min(jumps[j], jumps[i] + 1)
        return jumps[-1]


class Solution2:
    def jump(self, nums):
        min_jumps, max_reach, prev_max_reach = 0, 0, 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i >= prev_max_reach:
                prev_max_reach = max_reach
                min_jumps += 1
        return min_jumps


print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([0]))

