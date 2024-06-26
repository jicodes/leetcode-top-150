from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # The last element in postorder is the root of the tree
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find the root in inorder list to separate left and right subtrees
        mid = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1 :], postorder[mid:-1])

        return root
