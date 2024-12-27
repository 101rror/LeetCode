class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        mx = 0
        dp = [0] * n
        dp[0] = values[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], values[i - 1] + i - 1)
            mx = max(mx, dp[i] + values[i] - i)

        return mx