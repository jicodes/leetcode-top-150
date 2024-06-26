# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to simplify the code and a current pointer
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get the values from the current nodes, if any
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry
            total = val1 + val2 + carry

            # Update carry for the next iteration
            carry = total // 10

            # Create a new node with the digit value of the total
            current.next = ListNode(total % 10)

            # Move the current pointer to the next node
            current = current.next

            # Move to the next nodes in l1 and l2, if any
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the next node of the dummy, which is the head of the new list
        return dummy.next
