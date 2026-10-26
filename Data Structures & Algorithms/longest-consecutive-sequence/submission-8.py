class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best, streak = 0, 1
        _sorted = sorted(set(nums))

        if len(_sorted) == 0:
            return best
        if len(_sorted) == 1:
            return streak
        for i in range(len(_sorted) - 1):
            if _sorted[i + 1] - _sorted[i] != 1:
                streak = 1
            else: 
                streak += 1
            best = max(streak, best)
        return best