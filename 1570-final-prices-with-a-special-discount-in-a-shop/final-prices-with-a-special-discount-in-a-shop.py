class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []
        it = 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[i] >= prices[j]:
                    dif = prices[i] - prices[j]
                    ans.append(dif)
                    break
                if j == n - 1 and prices[i] < prices[j]:
                    ans.append(prices[i])

        ans.append(prices[-1])

        return ans
