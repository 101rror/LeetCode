class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)

        for j in range(1, n):
            dp3 = [0] * (n + 1)
            dp4 = [0] * (n + 1)
            for i in range(n + 1):
                prev = 0
                curr = sum(grid[x][j] for x in range(i))
                for y in range(n + 1):
                    if y > 0 and y <= i:
                        curr -= grid[y - 1][j]
                    if j > 0 and y > i:
                        prev += grid[y - 1][j - 1]
                    dp3[y] = max(dp3[y], prev + dp1[i], dp2[i])
                    dp4[y] = max(dp4[y], curr + dp2[i], curr + prev + dp1[i])

            dp1, dp2 = dp3, dp4

        return max(dp2)
