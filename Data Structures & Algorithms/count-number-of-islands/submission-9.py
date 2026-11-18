class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        DIRS = [(1,0), (-1, 0), (0,1), (0,-1)] # abajo, arriba, derecha, izq
        islands = 0
        visited = set()
        def dfs(r, c):
            if r >= rows or r < 0 or c < 0 or c >= cols or grid[r][c] == '0' or (r,c) in visited:                
                return 
            visited.add((r,c))
            for rx, cx in DIRS:
                dfs(rx + r, cx + c)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands