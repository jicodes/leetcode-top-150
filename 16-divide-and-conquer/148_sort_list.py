class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Find the middle point
        mid = self.getMiddle(head)
        left = head
        right = mid.next
        mid.next = None

        # Recursively sort the two halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves
        return self.merge(left, right)

    def getMiddle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        # At least one of left and right is now None
        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next
