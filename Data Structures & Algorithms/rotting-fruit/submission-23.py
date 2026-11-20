from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0), (0, 1), (0, -1), (1, 0)]
        rotten = deque()
        minutes = 0
        freshs = 0 
        marked = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                    marked.add((r,c))
                if grid[r][c] == 1:
                    freshs += 1
        
        def rot(r, c):
            nonlocal freshs
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if grid[r][c] == 0 or (r,c) in marked: return
            # is fresh
            marked.add((r, c))
            rotten.append((r,c))
            freshs -= 1

        while rotten and freshs:
            for _ in range(len(rotten)):
                (curr_a, curr_b) = rotten.popleft()
                for (a,b) in dirs:
                    rot(curr_a + a, curr_b + b)
            minutes += 1
        
        return minutes if freshs == 0 else -1

