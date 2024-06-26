from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count the total number of nodes in the list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Create a dummy node to simplify edge cases where the head might change
        group_prev = dummy = ListNode(next=head)
        prev = None
        curr = head  # Initialize curr to the head of the list

        while n >= k:
            # Decrease the node count by k since we will process k nodes
            n -= k
            # Reverse k nodes
            for _ in range(k):
                next_node = curr.next  # Store the next node
                curr.next = prev  # Reverse the current node's pointer
                prev = curr  # Move prev to the current node
                curr = next_node  # Move curr to the next node

            # Reconnect the reversed sublist with the rest of the list
            next_node = group_prev.next # The start of the current sublist (last node after reversal)
            group_prev.next.next = curr  # Connect the last node of the reversed sublist to the next node after the k-group
            group_prev.next = prev  # Connect the node before the sublist to the new head of the reversed sublist
            group_prev = next_node  # Move group_prev to the end of the reversed sublist

        return dummy.next  # Return the new head of the modified list
