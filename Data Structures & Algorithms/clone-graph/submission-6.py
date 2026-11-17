"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        stack = [node]
        res = {node: Node(node.val)}
        while stack:
            curr = stack.pop()
            for nei in curr.neighbors:
                if nei not in res:
                    res[nei] = Node(nei.val)
                    stack.append(nei)
                res[curr].neighbors.append(res[nei])
            
        return res[node]