class Solution:
    def largestMagicSquare(self, grid):
        n, m = len(grid), len(grid[0])

        row = [[0] * (m + 1) for _ in range(n)]
        col = [[0] * (n + 1) for _ in range(m)]
        d1 = [[0] * (m + 1) for _ in range(n + 1)]
        d2 = [[0] * (m + 2) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[j][i + 1] = col[j][i] + grid[i][j]
                d1[i + 1][j + 1] = d1[i][j] + grid[i][j]
                d2[i + 1][j] = d2[i][j + 1] + grid[i][j]

        for size in range(min(n, m), 1, -1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    s = row[i][j + size] - row[i][j]
                    if any(row[r][j + size] - row[r][j] != s for r in range(i, i + size)):
                        continue
                    if any(col[c][i + size] - col[c][i] != s for c in range(j, j + size)):
                        continue
                    if d1[i + size][j + size] - d1[i][j] != s:
                        continue
                    if d2[i + size][j] - d2[i][j + size] != s:
                        continue
                    return size
                    
        return 1
