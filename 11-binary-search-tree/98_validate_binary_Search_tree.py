# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Helper function to validate the BST with range limits
        def validate(node, low=float("-inf"), high=float("inf")):
            # If the node is None, it is a valid BST by definition
            if not node:
                return True
            # If the current node's value does not satisfy the BST property, return False
            if not (low < node.val < high):
                return False
            # Recursively validate the left subtree with an updated upper bound
            # Recursively validate the right subtree with an updated lower bound
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        # Start the validation from the root with the initial range limits
        return validate(root)
