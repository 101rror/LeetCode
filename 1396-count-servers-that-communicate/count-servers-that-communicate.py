class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        row = [0] * r
        col = [0] * c
        count = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        count += 1

        return count
