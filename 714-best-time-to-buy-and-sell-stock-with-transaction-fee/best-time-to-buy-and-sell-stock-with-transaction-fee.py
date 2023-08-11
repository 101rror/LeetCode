class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        pos = -prices[0]
        ans = 0

        for i in range(1, n):
            pos = max(pos, ans - prices[i])
            ans = max(ans, pos + prices[i] - fee)

        return ans