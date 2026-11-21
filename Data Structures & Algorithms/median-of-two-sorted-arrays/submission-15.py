class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):              # A siempre es el más corto
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2          # cuántos van a la izquierda

        l, r = 0, len(A)                 # i puede ir de 0 a len(A)
        while l <= r:
            i = (l + r) // 2             # cuántos toma A
            j = half - i                 # cuántos toma B

            L1 = A[i - 1] if i > 0 else float('-inf')
            R1 = A[i]     if i < len(A) else float('inf')
            L2 = B[j - 1] if j > 0 else float('-inf')
            R2 = B[j]     if j < len(B) else float('inf')

            if L1 > R2:                  # A aporta de más
                r = i - 1
            elif L2 > R1:                # A aporta de menos
                l = i + 1
            else:                        # corte correcto
                if total % 2 == 1:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2