class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set(nums)
        best = 0
        for n in _set:
            if n - 1 not in _set:
                streak = 1
                while n + streak in _set:
                    streak += 1
                best = max(streak, best)
        return best