# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')  # ✓ cualquier camino lo supera
        def diameter(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return 0
            left = max(0, diameter(root.left))
            right = max(0, diameter(root.right))
            res = max(res, root.val + left + right)
            return root.val + max(left, right)

        diameter(root)
        return res