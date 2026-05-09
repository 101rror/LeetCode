class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mn = min(m, n)

        for r in range(mn // 2):
            i = j = r
            vals = []

            for ni in range(j, n - j - 1):
                vals.append(grid[i][ni])
            for nj in range(i, m - i - 1):
                vals.append(grid[nj][n - j - 1])
            for ni in range(n - j - 1, j, -1):
                vals.append(grid[m - i - 1][ni])
            for nj in range(m - i - 1, i, -1):
                vals.append(grid[nj][j])

            nk = k % len(vals)
            vals = vals[nk:] + vals[:nk]

            x = 0
            for ni in range(j, n - j - 1):
                grid[i][ni] = vals[x]
                x += 1
            for nj in range(i, m - i - 1):
                grid[nj][n - j - 1] = vals[x]
                x += 1
            for ni in range(n - j - 1, j, -1):
                grid[m - i - 1][ni] = vals[x]
                x += 1
            for nj in range(m - i - 1, i, -1):
                grid[nj][j] = vals[x]
                x += 1

        return grid
