

from lctest import *

# 86. Partition List
# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node1 = dummy1 = ListNode(None)
        node2 = dummy2 = ListNode(None)

        node = head

        while node:
            if node.val < x:
                node1.next = node
                node1 = node
            else:
                node2.next = node
                node2 = node
            node = node.next

        node1.next = dummy2.next
        node2.next = None
        return dummy1.next


def verify_solution(*args):
    head = make_linked_list(args[0])
    print_linked_list(head)

    result = Solution().partition(head, args[1])
    print_linked_list(result)



verify_solution([1,4,3,2,5,2], 3)

