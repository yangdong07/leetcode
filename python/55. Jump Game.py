

# 55. Jump Game
# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

class Solution2:
    def canJump(self, nums):
        can_reach = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= can_reach:
                can_reach = i
        return can_reach == 0


class Backtracking:
    def canJump(self, nums):
        def can_jump(position):
            if position >= len(nums) - 1:
                return True

            furthest_jump = min(position + nums[position], len(nums) - 1)
            for j in range(position + 1, furthest_jump + 1):
                if can_jump(j):
                    return True
            return False
        return can_jump(0)


class TopDown:
    def canJump(self, nums):
        memo = [0] * len(nums)
        memo[-1] = 1   # -1, can't jump,  1, can jump

        def can_jump(position):
            if memo[position] == 1:
                return True
            elif memo[position] == -1:
                return False

            furthest_jump = min(position + nums[position], len(nums) - 1)
            for j in range(position + 1, furthest_jump + 1):
                if can_jump(j):
                    memo[j] = True
                    return True
            memo[position] = False
            return False
        return can_jump(0)


class BottomUp:
    def canJump(self, nums):
        memo = [False] * len(nums)
        memo[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i], len(nums) - 1) + 1):
                if memo[j]:
                    memo[i] = True
                    break

        return memo[0]


class Greedy:
    def canJump(self, nums):
        need_reach = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= need_reach:
                need_reach = i
        return need_reach == 0


print(BottomUp().canJump([0, 0]))
print(BottomUp().canJump([0]))
