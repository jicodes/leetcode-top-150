from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        before_left = dummy = ListNode(next=head)

        # Move `before_left` to the node before the reversal starts
        for _ in range(left - 1):
            before_left = before_left.next

        # Initialize pointers for the reversal
        prev = None
        curr = before_left.next

        # Reverse the sublist from left to right
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Reconnect the reversed sublist with the rest of the list
        before_left.next.next = curr  # Connect the original first node of the sublist to the rest of the list
        before_left.next = prev  # Connect the node before the sublist to the new head of the reversed sublist

        return dummy.next
