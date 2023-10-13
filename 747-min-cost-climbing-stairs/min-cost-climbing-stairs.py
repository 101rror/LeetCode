class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        ans = [0] * n

        for i in range(2, n):
            ans[i] = min(ans[i - 1] + cost[i - 1], ans[i - 2] + cost[i - 2])

        return ans[n - 1]