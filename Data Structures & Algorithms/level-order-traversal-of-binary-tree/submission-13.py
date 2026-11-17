# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        ans = []
        queue = deque([root]) if root else deque()
        
        while queue:
            lvl = []
            for _ in range(len(queue)):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(lvl)
        return ans