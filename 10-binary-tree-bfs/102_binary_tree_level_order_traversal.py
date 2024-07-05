from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()  # Remove the node from the queue
                current_level.append(
                    node.val
                )  # Add its value to the current level list

                # Add child nodes to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level's values to the result list
            result.append(current_level)

        return result
