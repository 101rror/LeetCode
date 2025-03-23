class Solution:
    def largestLocalUtil(self, grid, x, y):
        mx = 0

        for i in range(x, x + 3):
            for j in range(y, y + 3):
                mx = max(mx, grid[i][j])

        return mx

    def largestLocal(self, grid):
        n = len(grid)
        m = n - 2

        ans = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                ans[i][j] = self.largestLocalUtil(grid, i, j)

        return ans
