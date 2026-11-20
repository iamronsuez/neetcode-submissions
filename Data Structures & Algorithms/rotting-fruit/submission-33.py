from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0), (0, 1), (0, -1), (1, 0)]
        rotten = deque()
        minutes = 0
        freshs = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    rotten.append((r, c))
                if grid[r][c] == FRESH:
                    freshs += 1
        
        def rot(r, c):
            nonlocal freshs
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if grid[r][c] == EMPTY or grid[r][c] == ROTTEN: return
            # is fresh
            grid[r][c] = ROTTEN
            rotten.append((r,c))
            freshs -= 1
        
        while rotten and freshs:
            if freshs == 0: return 0
            for _ in range(len(rotten)):
                (curr_a, curr_b) = rotten.popleft()
                for (a,b) in dirs:
                    rot(curr_a + a, curr_b + b)
            minutes += 1
        
        return minutes if freshs == 0 else -1

