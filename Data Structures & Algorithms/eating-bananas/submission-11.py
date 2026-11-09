class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minsSpeed = 1
        left, right = 1, max(piles)

        while (left <= right):
            k = (left + right) // 2
            hoursPerPile = 0
            for p in piles:
                hoursPerPile += math.ceil(p / k)

            if hoursPerPile <= h:
                minsSpeed = k
                right = k - 1
            else:
                left = k + 1
        return minsSpeed