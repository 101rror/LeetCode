class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dp = defaultdict(int)
        for p in power:
            dp[p] += p
            dp[p - 3] = max(0, dp[p - 3])

        ans, last = 0, 0

        for p in sorted(dp.keys()):
            dp[p] = last = max(dp[p] + dp[p - 3], last)
            ans = max(ans, last)

        return ans
