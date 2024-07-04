class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")

        def max_gain(node):
            if not node:
                return 0

            # Recursively get the maximum gain from the left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Path sum that passes through the current node
            curr_path_sum = node.val + left_gain + right_gain

            # Update the global maximum sum if the curr path is better
            self.max_sum = max(self.max_sum, curr_path_sum)

            # Return the maximum gain the current node can add to its parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum
