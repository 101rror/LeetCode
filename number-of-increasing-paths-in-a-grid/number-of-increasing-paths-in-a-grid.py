class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = (10**9+7)

        @cache
        def dp(x, y):
            res = 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] > grid[x][y]:
                    res += dp(x+dx, y+dy)
            return res
        
        ret = 0
        for i in range(m):
            for j in range(n):
                ret += dp(i, j)

        ans = ret % mod

        return ans
                