class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mx = max(days)
        dp = [0] * (mx + 1)
        days = set(days)

        for i in range(1, mx + 1):
            if i in days:
                dp[i] = min(costs[2] + dp[max(i - 30, 0)], costs[1] +  dp[max(i - 7, 0)], costs[0] + dp[i - 1])
            else:
                dp[i] = dp[i - 1]
            
        return dp[-1]