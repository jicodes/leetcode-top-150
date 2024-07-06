# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # In-order traversal function
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Perform in-order traversal to get the sorted elements
        sorted_elements = inorder(root)
        # Return the k-th smallest element (1-indexed)
        return sorted_elements[k - 1]
