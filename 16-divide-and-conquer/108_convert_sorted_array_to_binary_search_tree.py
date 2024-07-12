from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to convert subarray to BST
        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Choose the middle element as the root using the improved method
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)

            return node

        # Call the helper function with the initial bounds
        return convert(0, len(nums) - 1)
