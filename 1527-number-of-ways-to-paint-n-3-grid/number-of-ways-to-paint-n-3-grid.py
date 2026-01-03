class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        x, y = 6, 6

        for i in range(2, n + 1):
            nx = (3 * x + 2 * y)
            ny = (2 * x + 2 * y)
            x, y = nx, ny

        return (x + y) % MOD
