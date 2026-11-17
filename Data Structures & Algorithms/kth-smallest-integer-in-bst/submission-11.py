# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def kthSmallest(self, root, k):
    def dfs(node, k):
        if not node:
            return k, None                  # nada que contar
        k, res = dfs(node.left, k)          # 1. la izquierda me devuelve cuánto quedó
        if res is not None:
            return k, res                   #    ya la encontró abajo: la subo
        k -= 1                              # 2. cuento este nodo
        if k == 0:
            return k, node.val              #    soy el k-ésimo
        return dfs(node.right, k)           # 3. sigo con la derecha

    return dfs(root, k)[1]