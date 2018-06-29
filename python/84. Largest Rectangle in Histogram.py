

# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution1:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        for i, h in enumerate(heights):
            # find left
            l = i - 1
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            l += 1

            # find right
            r = i + 1
            while r < len(heights) and heights[i] <= heights[r]:
                r += 1

            max_area = max(max_area, h * (r - l))

        return max_area



class Solution2:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [0] * n
        right = [n] * n

        for i in range(1, n):
            p = i - 1
            h = heights[i]
            while p >= 0 and heights[p] >= h:
                p = left[p] - 1
            left[i] = p + 1

        for i in range(n - 2, -1, -1):
            p = i + 1
            h = heights[i]
            while p < n and heights[p] >= h:
                p = right[p]
            right[i] = p

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i]))

        return ans


class Solution3_1:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = i = 0
        while i < len(heights):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                j = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, heights[j] * width)

        while stack:
            j = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, heights[j] * width)

        return max_area

class Solution3_2:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        max_area = 0
        heights.append(0)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area


class Solution3_3:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        max_area = 0
        heights.append(0)
        stack = [0] * len(heights)
        n = 0
        for i in range(len(heights)):
            while n and heights[stack[n - 1]] > heights[i]:
                # print(stack[:n])
                n -= 1
                h = heights[stack[n]]
                w = i - stack[n - 1] - 1 if n else i
                max_area = max(max_area, h * w)
            stack[n] = i
            n += 1

        return max_area



Solution = Solution1

print(Solution().largestRectangleArea([2,1,5,6,2,3]))  # 10
# print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([1]))
print(Solution().largestRectangleArea([2, 1, 2]))  # 3
print(Solution().largestRectangleArea([1, 1]))  # 2
print(Solution().largestRectangleArea([5,4,1,2]))  # 8
print(Solution().largestRectangleArea([4,2,0,3,2,5]))  # 8