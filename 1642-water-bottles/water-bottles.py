class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        bot, exc = numBottles, numExchange

        while bot:
            x = bot // exc
            y = bot - (exc * x)
            ans += x
            bot //= exc
            bot += y

            if bot < exc:
                return ans
