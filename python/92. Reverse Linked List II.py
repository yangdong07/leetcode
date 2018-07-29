
# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii

from lctest import *


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev = dummy = ListNode(None)
        node = dummy.next = head
        index = 1

        while index < m:
            node, prev = node.next, node
            index += 1

        # node is @m, prev is @m-1
        break_prev = prev
        break_head = node

        while index <= n:
            prev, node.next, node = node, prev, node.next
            index += 1

        # node is @n+1, prev is @n
        break_head.next = node
        break_prev.next = prev

        return dummy.next



def verify_solution(*args):
    head = make_linked_list(args[0])
    print_linked_list(head)

    head = Solution().reverseBetween(head, args[1], args[2])
    print_linked_list(head)


verify_solution([1,2,3,4,5], 2, 4)