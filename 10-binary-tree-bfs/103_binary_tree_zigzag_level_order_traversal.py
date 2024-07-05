from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True  # Variable to track the direction of traversal

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = (
                deque()
            )  # Using deque to allow efficient insertion at both ends

            for _ in range(level_size):
                node = queue.popleft()  # Remove the node from the queue

                # Add the node's value to the current level based on the traversal direction
                if left_to_right:
                    current_level.append(node.val)  # Append to the right end
                else:
                    current_level.appendleft(node.val)  # Append to the left end

                # Add child nodes to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level's values to the result list
            result.append(list(current_level))
            left_to_right = not left_to_right  # Toggle the direction for the next level

        return result
