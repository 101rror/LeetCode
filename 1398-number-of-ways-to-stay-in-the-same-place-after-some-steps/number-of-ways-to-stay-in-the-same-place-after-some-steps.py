class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        Mod = 10**9 + 7
        n = min(steps, arrLen)
        dp = [1] + [0]*n

        while steps:
            prev = 0
            for i in range(n):
                cur = dp[i]
                dp[i] = (cur + dp[i+1] + prev) % Mod
                prev = cur
                
            steps -= 1

        return dp[0]

        