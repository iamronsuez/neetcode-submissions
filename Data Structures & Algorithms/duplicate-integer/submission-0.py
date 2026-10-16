class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearances = set()
        
        for i in range(len(nums)):
            if nums[i] in appearances:
                return True
            appearances.add(nums[i])
        return False