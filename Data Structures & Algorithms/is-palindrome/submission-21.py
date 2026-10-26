class Solution:
    def isPalindrome(self, s: str) -> bool:
        _currentIndex = 0
        _endIndex = len(s) - 1

        while (_currentIndex < _endIndex):
            if not s[_currentIndex].isalnum():
                _currentIndex += 1
            elif not s[_endIndex].isalnum():
                _endIndex -= 1
            else:
                if s[_currentIndex].lower() != s[_endIndex].lower():
                    return False
                _endIndex -= 1
                _currentIndex += 1
        return True