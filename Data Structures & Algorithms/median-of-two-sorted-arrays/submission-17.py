class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        INF = float('inf')
        A, B = nums1, nums2
        if len(A) > len(B):              # A siempre es el más corto
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2
        A = [-INF] + A + [INF]                        # bordes ya puestos
        B = [-INF] + B + [INF]
        l, r = 0, len(A) - 2
        while True:
            i = (l + r) // 2
            j = half - i
            if A[i] > B[j + 1]:   r = i - 1           # L1 > R2
            elif B[j] > A[i + 1]: l = i + 1           # L2 > R1
            else: break
        left = max(A[i], B[j])
        return left if total % 2 else (left + min(A[i + 1], B[j + 1])) / 2