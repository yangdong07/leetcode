

# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle

class Solution1:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = []
            for i in range(n + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area


class Solution2:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        nums = [int(''.join(row), base=2) for row in matrix]
        # print(nums)

        max_area = 0
        for i in range(len(nums)):
            j = i
            num = nums[i]
            while j < len(nums):
                # print(num, nums[j])
                num = num & nums[j]
                if num == 0:
                    break
                cur_num = num
                l = 0
                # print i,j,cur_num
                while cur_num != 0:
                    l += 1
                    cur_num = cur_num & (cur_num << 1)
                    # print(cur_num)
                max_area = max(max_area, l * (j - i + 1))
                j += 1

        return max_area


print(Solution2().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))



