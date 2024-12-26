class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        mod = 10**9 + 7

        dp[0] = 1

        for num in range(1, n + 1):
            m = num**x
            for i in range(n, 0, -1):
                c = i - m
                if c >= 0:
                    dp[i] += dp[c]
                    dp[i] %= mod

        return dp[n]
