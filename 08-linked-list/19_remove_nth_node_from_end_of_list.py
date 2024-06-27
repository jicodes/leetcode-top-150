from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node which points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both first and second pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        # Return the head of the modified list
        return dummy.next
