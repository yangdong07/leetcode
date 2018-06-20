

# 57. Insert Interval
# https://leetcode.com/problems/insert-interval

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str([self.start, self.end])


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left.append(i)
            elif i.start > e:
                right.append(i)
            else:
                s = min(s, i.start)
                e = max(e, i.end)

        return left + [Interval(s, e)] + right


class Solution2:
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = []

        r = len(intervals)
        for c, i in enumerate(intervals):
            if i.end < s:
                left.append(i)
            elif i.start > e:
                r = c
                break
            else:
                s = min(s, i.start)
                e = max(e, i.end)

        return left + [Interval(s, e)] + intervals[r:]

intervals = [Interval(x[0], x[1]) for x in [[1,3],[2,6],[8,10],[15,18]]]

print(intervals)
print(Solution().insert(intervals, Interval(4, 16)))