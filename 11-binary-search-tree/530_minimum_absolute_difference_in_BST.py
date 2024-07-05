from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = -float("inf")
        self.min_diff = float("inf")

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)  # Traverse left subtree

            # Process current node
            curr_diff = node.val - self.prev
            if curr_diff < self.min_diff:
                self.min_diff = curr_diff
            self.prev = node.val

            inorder(node.right)  # Traverse right subtree

        inorder(root)
        return self.min_diff
