class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, current in enumerate(nums):
            diff = target - current
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[current] = i