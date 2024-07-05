from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        averages = []

        while queue:
            level_sum = 0
            level_size = len(queue)  # Number of nodes at the current level

            for _ in range(level_size):
                node = queue.popleft()  # Remove the node from the queue
                level_sum += node.val  # Add its value to the sum

                # Add child nodes to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the average for this level
            averages.append(level_sum / level_size)

        return averages
