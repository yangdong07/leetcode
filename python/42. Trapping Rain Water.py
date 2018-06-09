

# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water

# brute force
class Solution1:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ans = 0
        for i in range(1, len(height) - 1):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]

        return ans


#
class Solution2:
    def trap(self, height):

        if not height:
            return 0

        ans = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        max_left[0] = height[0]
        max_right[-1] = height[-1]

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        for i in range(1, len(height) - 1):
            ans += min(max_left[i], max_right[i]) - height[i]
        return ans



class Solution3:
    def trap(self, height):

        l, r = 0, len(height) - 1
        max_left = max_right = ans = 0

        while l < r:
            if height[l] < height[r]:
                if max_left <= height[l]:
                    max_left = height[l]
                else:
                    ans += max_left - height[l]
                l += 1
            else:
                if max_right <= height[r]:
                    max_right = height[r]
                else:
                    ans += max_right - height[r]
                r -= 1
        return ans



print(Solution3().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
