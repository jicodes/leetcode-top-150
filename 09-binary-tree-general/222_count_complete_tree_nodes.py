class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            # Left subtree is a perfect binary tree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree, but one level shallower than the left subtree
            return (1 << right_height) + self.countNodes(root.left)


# Example usage:
# Construct a complete binary tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#   / \
#  8   9
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

sol = Solution()
print(sol.countNodes(root))  # Output: 9
