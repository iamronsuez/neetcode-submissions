class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # 1) bajar a la izquierda todo lo posible
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2) sacar el más pequeño pendiente
            curr = stack.pop()

            # 3) visitarlo
            k -= 1
            if k == 0:
                return curr.val

            # 4) girar a la derecha
            curr = curr.right