class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        # Start with the root node
        curr_level_head = root

        # Dummy node that helps to build the next level
        dummy = Node(0)  # Create the dummy node
        tail = dummy  # Initialize tail to dummy
        dummy.next = None  # Reset the dummy next to None

        while curr_level_head:
            # Iterate over the current level
            curr_node = curr_level_head
            dummy.next = None  # Reset the dummy for the next level
            tail = dummy  # Reset tail to dummy at the start of each level

            while curr_node:
                if curr_node.left:
                    tail.next = curr_node.left  # Connect the left child
                    tail = tail.next  # Move the tail to the connected child
                if curr_node.right:
                    tail.next = curr_node.right  # Connect the right child
                    tail = tail.next  # Move the tail to the connected child

                # Move to the next node in the current level using the next pointer
                curr_node = curr_node.next

            # Move to the next level
            curr_level_head = dummy.next

        return root


# The line of code that updates `dummy.next` to the first node of the next level is:

# tail.next = curr_node.left # or
# tail.next = curr_node.right
