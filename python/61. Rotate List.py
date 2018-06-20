

# 61. Rotate List
# https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        cache = []
        cursor = head
        while cursor:
            cache.append(cursor)
            cursor = cursor.next

        if not cache:
            return head

        k = k % len(cache)

        if k == 0:
            return head

        cache[~k].next = None
        cache[-1].next = cache[0]
        return cache[-k]


class Solution2:
    def rotateRight(self, head, k):
        if not head:
            return None

        n = 1
        cursor = head
        while cursor.next:
            n += 1
            cursor = cursor.next

        k = k % n
        if k == 0:
            return head

        cursor.next = head
        cursor = head
        for i in range(n - k - 1):
            cursor = cursor.next
        head = cursor.next
        cursor.next = None

        return head