class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            current = nums[i]
            for j in range(i + 1, length - 1):
                if current + nums[j] == target:
                    return [i, j]
        return [0,0]