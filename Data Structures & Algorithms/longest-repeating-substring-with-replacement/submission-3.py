class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1          # entra la letra nueva

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1       # primero: la letra de la izquierda sale
                left += 1                 # después: se mueve el borde
            best = max(best, right - left + 1)                              # largo de la ventana
        return best