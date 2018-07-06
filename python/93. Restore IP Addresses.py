

# 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses

class Solution1:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        n = len(s)

        def dfs(d, i, p):

            if d == 5:
                # ip = '.'.join([s[:p[0]], s[p[0]:p[1]], s[p[1]:p[2]], s[p[2]:]])
                # print(ip, i, n)
                if i == n:
                    ip = '.'.join([s[:p[0]], s[p[0]:p[1]], s[p[1]:p[2]], s[p[2]:]])
                    results.append(ip)
                return

            if i >= n:
                return

            dfs(d + 1, i + 1, p + [i + 1])
            if s[i] != "0":
                dfs(d + 1, i + 2, p + [i + 2])
                if int(s[i:i + 3]) < 256:
                    dfs(d + 1, i + 3, p + [i + 3])
        dfs(0, 0, [])
        return results


class Solution2:
    def restoreIpAddresses(self, s):
        results = []
        n = len(s)

        def dfs(d, i, ip):

            if d == 4:
                if i == n:
                    results.append(ip[:-1])
                return

            if i < n:
                dfs(d + 1, i + 1, ip + s[i:i+1] + '.')
            if i < n - 1 and s[i] != "0":
                dfs(d + 1, i + 2, ip + s[i:i+2] + '.')
                if i < n - 2 and int(s[i:i+3]) < 256:
                    dfs(d + 1, i + 3, ip + s[i:i+3] + '.')
        dfs(0, 0, '')
        return results

Solution = Solution2
print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("1111"))
print(Solution().restoreIpAddresses("010010"))