# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def serialize(node):
            if not node:
                return ",#"                     # marcador de None
            return "," + str(node.val) + serialize(node.left) + serialize(node.right)
            
        return serialize(subRoot) in serialize(root)

    