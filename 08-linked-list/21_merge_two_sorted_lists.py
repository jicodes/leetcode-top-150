# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify the merge process
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # If there are remaining nodes in l1 or l2, append them
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        # Return the merged list, which starts at dummy.next
        return dummy.next
