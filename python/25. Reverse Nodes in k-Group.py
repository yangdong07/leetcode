

# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def swapNodes(prev):
            """
            given prev node, return nodes swapped
            prev -> 1 -> 2 -> 3 -> 4 -> 5 -> last, return last <- 1 <- 2 <- 3 <- 4 <- 5 <- prev,  return new_prev 1.
            """
            last = first = prev.next
            for i in range(k):
                if last is None:
                    return None
                last = last.next

            n1 = first
            n2 = first.next
            for i in range(k-1):
                n1, n2.next, n2 = n2, n1, n2.next

            prev.next = n1
            first.next = last

            return first

        node = dummy = ListNode(0)
        dummy.next = head
        while node:
            node = swapNodes(node)

        return dummy.next


def generateListNodes(l):
    head = ListNode(l[0])
    prev = head
    for n in l[1:]:
        prev.next = ListNode(n)
        prev = prev.next
    return head


def printListNodes(l):
    while l:
        print(l.val, end='->')
        l = l.next

print()
list_nodes = generateListNodes([1, 2,3, 4, 6, 5])
printListNodes(list_nodes)

print()

new_list_nodes = Solution().reverseKGroup(list_nodes, 3)

printListNodes(new_list_nodes)