
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_linked_list(nums):

    node = dummy = ListNode(None)

    for n in nums:
        node.next = ListNode(n)
        node = node.next
    return dummy.next


def print_linked_list(head):

    node = head
    while node and node.next:
        print(node.val, end=' -> ')
        node = node.next
    print(node.val)

