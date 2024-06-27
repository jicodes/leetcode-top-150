from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes
        less_head = ListNode(0)
        greater_head = ListNode(0)

        # Pointers for the less and greater lists
        less = less_head
        greater = greater_head

        # Traverse the original list
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next

        # Connect the less list to the greater list
        greater.next = None
        less.next = greater_head.next

        # Return the head of the partitioned list
        return less_head.next
