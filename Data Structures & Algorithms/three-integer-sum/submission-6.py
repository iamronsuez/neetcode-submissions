class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        _sorted = sorted(nums)
        _triplets = set()
        for i, current in enumerate(_sorted):
            left, right = i + 1, len(_sorted) - 1
            while left < right:
                if _sorted[left] + _sorted[right] + current > 0:
                    right -= 1
                elif _sorted[left] + _sorted[right] + current < 0:
                    left +=1
                else:
                    if not (current, _sorted[left], _sorted[right]) in _triplets:
                        _triplets.add((current, _sorted[left], _sorted[right]))
                    right -=1
                    left += 1
        return [list(t) for t in _triplets]