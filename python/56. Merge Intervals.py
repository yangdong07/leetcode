

# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str([self.start, self.end])

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []

        for i in sorted(intervals, key=lambda x: x.start):
            if ans and i.start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, i.end)
            else:
                ans.append(i)
        return ans

intervals = [Interval(x[0], x[1]) for x in [[1,3],[2,6],[8,10],[15,18]]]

print(intervals)
print(Solution().merge(intervals))