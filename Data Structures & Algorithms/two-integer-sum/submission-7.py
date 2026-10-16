class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            current = nums[i]
            for j in range(length - 1):
                if current + nums[j + 1] == target:
                    return [i, j + i]
        return [0,0]