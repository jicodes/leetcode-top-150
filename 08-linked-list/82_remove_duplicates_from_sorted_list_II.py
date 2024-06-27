from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node which points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # If the current node has duplicates
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Connect the previous node to the node after the duplicates
                prev.next = head.next
            else:
                # No duplicate, move prev to the current node
                prev = prev.next
            # Move head to the next node
            head = head.next

        return dummy.next
