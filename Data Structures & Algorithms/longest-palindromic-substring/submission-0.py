class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        best = ""
        for i in range(len(s)):            
            for left, right in [(i, i), (i, i + 1)]:
                while (left >= 0 and right < len(s)):
                    if s[left] != s[right]:
                        break
                    left -= 1
                    right += 1
                
                if len(s[left + 1: right]) > len(best):
                    best = s[left + 1: right]
        return best
