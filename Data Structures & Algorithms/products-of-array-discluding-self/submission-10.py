class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before, after= [], []
        _total = 1
        for ix in nums:
            before.append(_total)
            _total *= ix

        _total = 1
        for jx in reversed(nums):
            after.append(_total)
            _total *= jx

        return [a * b for a, b in zip(before, reversed(after))]