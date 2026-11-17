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
        res = {}
        def dfs(n):
            if n in res:
                return res[n]
            copy = Node(n.val)
            res[n] = copy               # se registra ANTES de recorrer los vecinos, para cortar los ciclos
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)

        