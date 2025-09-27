class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(1, 4):
                jmp = i + j
                if jmp <= n:
                    dp[jmp] = min(dp[jmp], dp[i] + costs[jmp - 1] + (jmp - i) ** 2)

        return dp[n]
