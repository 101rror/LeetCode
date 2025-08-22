class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        left = up = sys.maxsize
        right = down = -sys.maxsize

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    left = min(left, j)
                    up = min(up, i)
                    right = max(right, j)
                    down = max(down, i)

        ans = (right - left + 1) * (down - up + 1)
        return ans
