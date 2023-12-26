class Solution:
    def numRollsToTarget(self, n: int, k: int, tar: int) -> int:
        if n * k < tar:
            return 0
        if n == 1 or n * k == tar:
            return 1

        mod = int(10 ** 9 + 7)

        dp = [[0] * (tar + 1) for _ in range(n + 1)]

        for j in range(1, min(k + 1, tar + 1)):
            dp[1][j] = 1
        for i in range(2, n + 1):
            for j in range(1, tar + 1):
                for x in range(1, k + 1):
                    if j - x >= 0:
                        dp[i][j] += dp[i - 1][j - x]

                dp[i][j] %= mod 

        return dp[-1][-1]