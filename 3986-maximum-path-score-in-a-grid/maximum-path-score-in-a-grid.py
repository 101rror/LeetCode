class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        prev = [[-1] * (k + 1) for _ in range(n)]
        curr = [[-1] * (k + 1) for _ in range(n)]
        prev[0][0] = 0

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cost = 1 if val in (1, 2) else 0
                score = val

                for c in range(cost, k + 1):
                    best = -1
                    if j > 0 and curr[j - 1][c - cost] != -1:
                        v = curr[j - 1][c - cost] + score
                        if v > best:
                            best = v
                    if prev[j][c - cost] != -1:
                        v = prev[j][c - cost] + score
                        if v > best:
                            best = v
                    curr[j][c] = best

            prev, curr = curr, [[-1] * (k + 1) for _ in range(n)]

        return max(prev[n - 1])
