class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # se hace el merge de los arrays
        n = len(nums1)
        m = len(nums2)
        total = n + m
        mid = total // 2
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i +=1
            else:
                merged.append(nums2[j])
                j +=1
        merged += nums1[i:] + nums2[j:]


        if total % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid - 1]) / 2

