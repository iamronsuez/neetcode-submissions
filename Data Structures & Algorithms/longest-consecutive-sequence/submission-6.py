class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best, streak = 0, 0
        _sorted = sorted(set(nums))

        if len(_sorted) == 0:
            return 0
        if len(_sorted) == 1:
            return 1
        for i in range(len(_sorted) - 1):
            if _sorted[i + 1] - _sorted[i] != 1:
                streak = 0
            else: 
                streak += 1
            best = max(streak + 1, best)
        return best