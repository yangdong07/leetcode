

# 77. Combinations
# https://leetcode.com/problems/combinations

class Solution1:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [list(range(1, k + 1))]

        sub = self.combine(n - 1, k - 1)
        for c in sub:
            c.append(n)
        return sub + self.combine(n - 1, k)

        # return [c + [n] for c in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)

        # return [c + [i] for i in range(k, n + 1) for c in self.combine(i - 1, k - 1)]


class Solution2:
    def combine(self, n, k):
        combinations = [[i] for i in range(1, n + 1)]
        for _ in range(k - 1):
            combinations = [[i] + c for c in combinations for i in range(k, c[0])]
        return combinations


class Solution22:
    def combine(self, n, k):
        combinations = [[i] for i in range(1, n + 1)]
        for _ in range(k - 1):
            combinations = [c + [i] for c in combinations for i in range(c[-1] + 1, n + 1)]
        return combinations


class Solution3(object):
    def combine(self, n, k):
        ans = []
        stack = list(range(1, k + 1))
        choice = k + 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])       # find a combination
            if l == k or choice > n - k + l + 1:  # go back if choice + k - l - 1 > n;
                if not stack:
                    return ans
                choice = stack.pop() + 1
            else:
                stack.append(choice)       # append choice
                choice += 1


class Solution4(object):
    def combine(self, n, k):
        ans = {}

        def _combine(m, j):
            if (m, j) in ans:
                return ans[(m, j)]
            if j == 1:
                ans[(m, j)] = [[i] for i in range(1, m + 1)]
            elif j == m:
                ans[(m, j)] = [list(range(1, j + 1))]
            else:
                sub = _combine(m - 1, j - 1)
                for c in sub:
                    c.append(m)
                ans[(m, j)] = sub + self.combine(m - 1, j)

            return ans[(m, j)]

        return _combine(n, k)


from itertools import combinations
class Solution5:
    def combine(self, n, k):
        return list(combinations(range(1, n + 1), k))


class Solution6(object):
    def combine(self, n, k):
        ans = []
        stack = list(range(1, k + 1))
        choice = k + 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])       # find a combination
            if l == k or choice > n - k + l + 1:  # go back if choice + k - l - 1 > n;
                if not stack:
                    return ans
                choice = stack.pop() + 1
            else:
                stack.extend(range(choice, choice + k - l))       # append choice

Solution = Solution6

print(Solution().combine(4, 2))
print(Solution().combine(4, 4))
print(Solution().combine(6, 4))