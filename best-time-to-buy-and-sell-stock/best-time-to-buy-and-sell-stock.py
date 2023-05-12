class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        j = 0

        for i in range(0, n):
            if (prices[j] > prices[i]):
                j = i
            else:
                res = (prices[i] - prices[j])
                ans = max(ans, res)

        return ans