# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_number):
            if not node:
                return 0

            current_number = current_number * 10 + node.val

            # If it's a leaf, return the current number
            if not node.left and not node.right:
                return current_number

            # Otherwise, proceed to the left and right subtrees
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            return left_sum + right_sum

        return dfs(root, 0)


# Example Usage
# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# solution = Solution()
# result = solution.sumNumbers(tree)
# print(result)  # Output: 25 (12 + 13)
