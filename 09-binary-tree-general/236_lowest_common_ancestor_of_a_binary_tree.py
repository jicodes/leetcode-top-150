class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Base case: If the root is None or it matches with either p or q, return root
        if not root or root == p or root == q:
            return root

        # Recursively search for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-None, the current node is the LCA
        if left and right:
            return root
        # If only one side is non-None, return that side
        elif left:
            return left
        else:
            return right


# Example usage:
# Construct the binary tree:
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()
p = root.left  # Node 5
q = root.left.right.right  # Node 4
lca = sol.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 5
