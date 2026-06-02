class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n = len(cost)
        ans, x = 0, 0

        for i in range(n):
            if x < 2:
                ans += cost[i]
                x += 1
            else:
                x = 0

        return ans
