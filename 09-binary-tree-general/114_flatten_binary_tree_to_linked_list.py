class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)

        # Store the right subtree
        right_subtree = root.right

        # If there's a left subtree, we insert it between the root and the right subtree
        if root.left:
            root.right = root.left
            root.left = None

            # Move to the end of the new right subtree
            current = root.right
            while current.right:
                current = current.right

            # Attach the original right subtree
            current.right = right_subtree


# Example Usage
# Construct the binary tree [1,2,5,3,4,null,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

sol = Solution()
sol.flatten(root)

# Now the tree should be flattened to 1->2->3->4->5->6
