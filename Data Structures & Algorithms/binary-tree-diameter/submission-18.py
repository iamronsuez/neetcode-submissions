# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        height(root)
        return res