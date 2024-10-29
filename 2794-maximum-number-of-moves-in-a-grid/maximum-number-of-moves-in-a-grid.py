class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m, dirs = len(grid), len(grid[0]), [(0,1),(1,1),(-1,1)]

        @cache
        def dfs(i, j):
            moves = 0
            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < n and nj < m and grid[i][j] < grid[ni][nj]:
                    moves = max(moves, 1 + dfs(ni, nj))

            return moves

        return max(dfs(i, 0) for i in range(n))