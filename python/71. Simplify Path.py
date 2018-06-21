

# 71. Simplify Path
# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        segments = path.split('/')

        i = 0
        for seg in segments:
            if seg == '.' or seg == '':
                continue
            elif seg == '..':
                i = max(0, i - 1)
            else:
                segments[i] = seg
                i += 1

        return '/' + '/'.join(segments[:i])

print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/a/./b/../../c/"))
print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/home//foo/"))