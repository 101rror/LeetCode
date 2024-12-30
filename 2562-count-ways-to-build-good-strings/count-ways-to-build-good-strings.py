class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)

        for i in range(high, -1, -1):
            dp[i] += int(low <= i <= high)
            if i + zero <= high:
                dp[i] += dp[i + zero]
            if i + one <= high:
                dp[i] += dp[i + one]

        return dp[0] % mod
