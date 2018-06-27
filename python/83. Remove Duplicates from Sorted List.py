

# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        distinct = dummy = ListNode(None)
        current = head

        while current:
            if current.val != distinct.val:
                distinct.next = current
                distinct = current
            current = current.next

        distinct.next = None

        return dummy.next


class Solution2:
    def deleteDuplicates(self, head):
        p = head
        while p:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head


def lctest(nums):
    if not nums:
        assert Solution().deleteDuplicates(None) == None
        return

    prev = head = ListNode(nums[0])

    for n in nums[1:]:
        prev.next = ListNode(n)
        prev = prev.next

    curr = head

    while curr:
        print(curr.val, end='->')
        curr = curr.next
    print()

    result = Solution().deleteDuplicates(head)

    curr = result

    while curr:
        print(curr.val, end='->')
        curr = curr.next
    print()

lctest([1, 1, 2, 3, 3, 4, 5, 5, 6])
