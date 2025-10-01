class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles > 1:
            x = numBottles // numExchange
            y = numBottles - (numExchange * x)
            ans += x
            numBottles = numBottles // numExchange
            numBottles += y

            if numBottles < numExchange:
                break

        return ans
