class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count, rows, cols = 0, len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 4

                    if r > 0 and grid[r-1][c] == 1:
                        count -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        count -= 2
                        
        return count