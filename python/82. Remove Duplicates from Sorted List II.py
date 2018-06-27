

# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

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

        dummy = ListNode(None)
        distinct = previous = dummy
        dummy.next = current = head

        duplicate = True

        while current:
            if current.val == previous.val:
                duplicate = True
            else:
                if not duplicate:
                    distinct.next = previous
                    distinct = distinct.next
                duplicate = False
                previous = current
            current = current.next

        if not duplicate:
            distinct.next = previous
            distinct = distinct.next

        distinct.next = None

        return dummy.next


class Solution2:
    def deleteDuplicates(self, head):

        dummy = ListNode(None)
        distinct = dummy
        dummy.next = current = head

        while current:
            val = current.val
            if current.next and current.next.val == val:
                current = current.next.next
                while current and current.val == val:
                    current = current.next
            else:
                distinct.next = current
                distinct = current
                current = current.next

        distinct.next = None
        return dummy.next


Solution = Solution2

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
