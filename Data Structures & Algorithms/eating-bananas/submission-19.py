from bisect import bisect_left

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speeds = range(1, max(piles) + 1)
        alcanza = lambda k: sum(math.ceil(p / k) for p in piles) <= h
        return bisect_left(speeds, True, key=alcanza) + 1