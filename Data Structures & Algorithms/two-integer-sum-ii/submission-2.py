class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _currentIndex = 0
        _endIndex = len(numbers) - 1
 
        while (_currentIndex < _endIndex):
                if numbers[_currentIndex] + numbers[_endIndex] > target:
                    _endIndex -= 1
                elif numbers[_currentIndex] + numbers[_endIndex] < target:
                    _currentIndex += 1
                else:
                    if numbers[_currentIndex] + numbers[_endIndex] == target:
                        return [_currentIndex + 1, _endIndex+1]
        return []