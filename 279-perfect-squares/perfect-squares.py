class Solution:
    def numSquares(self, n: int) -> int:
        minval = float('inf')
        dp = [minval] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            mn = minval
            x = 1
            while (x ** 2 <= i):
                mn = min(mn, dp[i - x ** 2] + 1)
                x += 1

            dp[i] = mn

        return dp[n]
