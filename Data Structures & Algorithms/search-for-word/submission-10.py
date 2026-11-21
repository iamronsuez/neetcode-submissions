class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        letters = len(word)
        SEEN = '#'
        # row, column, kth letter
        def dfs(r, c, k):
            if k == letters : return True
            if r < 0 or r >= rows or c < 0 or c >=cols: return False
            if word[k] != board[r][c]: return False
            board[r][c] = SEEN
            found = False
            for a, b in DIRS:
                if dfs(r + a, c + b, k + 1):
                    found = True
                    break                         # sale del FOR, no de la función
            board[r][c] = word[k]         # se ejecuta igual
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
