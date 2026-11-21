class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        rows = len(board)
        cols = len(board[0])
        letters = len(word)
        # row, column, kth letter
        def dfs(r, c, k):
            if k == letters : return True
            if r < 0 or r >= rows or c < 0 or c >=cols: return False
            if word[k] != board[r][c] or (r,c) in seen: return False
            seen.add((r,c))
            for a,b in DIRS:
                if dfs( r + a, c + b, k + 1):
                    return True
            seen.remove((r,c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
