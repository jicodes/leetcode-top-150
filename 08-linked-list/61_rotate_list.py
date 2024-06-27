from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Compute the length of the linked list
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        # Compute the effective rotations needed
        k = k % length
        if k == 0:
            return head

        # Find the new tail, which is (length - k - 1) steps from the start
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # The new head is new_tail.next
        new_head = new_tail.next

        # Break the link
        new_tail.next = None

        # Connect the end of the list to the original head
        curr.next = head

        return new_head
