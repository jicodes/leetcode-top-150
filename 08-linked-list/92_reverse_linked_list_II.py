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
        if not head or left == right:
            return head

        # Create a dummy node to simplify edge cases where reversing starts at head
        dummy = ListNode(0, head)
        pre = dummy

        # Move `pre` to the node before the reversal starts
        for _ in range(left - 1):
            pre = pre.next

        # Reverse the sublist from left to right
        reverse_start = pre.next
        then = reverse_start.next

        # Perform the sublist reversal
        for _ in range(right - left):
            reverse_start.next = then.next
            then.next = pre.next
            pre.next = then
            then = reverse_start.next

        return dummy.next
