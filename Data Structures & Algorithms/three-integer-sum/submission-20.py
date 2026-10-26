class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        _sorted = sorted(nums)
        _triplets = []
        for i, current in enumerate(_sorted):
            left, right = i + 1, len(_sorted) - 1
            if i > 0 and _sorted[i - 1] == current:
                continue
            while left < right:
                if _sorted[left] + _sorted[right] + current > 0:
                    right -= 1
                elif _sorted[left] + _sorted[right] + current < 0:
                    left +=1
                else:
                    _triplets.append([current, _sorted[left], _sorted[right]])
                    right -=1
                    left += 1
                    while left < right and _sorted[left] == _sorted[left - 1]:
                        left += 1
        return _triplets