

# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams

import collections

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        for s in strs:
            k = ''.join(sorted(s))
            if k not in groups:
                groups[k] = [s]
            else:
                groups[k].append(s)

        return list(groups.values())

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            k = tuple(count)
            if k not in groups:
                groups[k] = [s]
            else:
                groups[k].append(s)

        return list(groups.values())

