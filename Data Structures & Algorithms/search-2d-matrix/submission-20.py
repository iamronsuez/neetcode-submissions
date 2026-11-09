class Solution:
    def searchRow(self, matrix: List[List[int]], target: int):
        left = 0
        right = len(matrix) - 1
        while (left <= right):  
            mid = (left + right) // 2   
            if (target < matrix[mid][0]):
                right = mid - 1
            elif (target > matrix[mid][-1]):
                left = mid + 1
            else:
                return matrix[mid]
        return []

    def searchWithinRow(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if (nums[mid] == target):
                return True     
            if (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchWithinRow(self.searchRow(matrix, target), target)