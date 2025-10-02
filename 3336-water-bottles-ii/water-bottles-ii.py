class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        bot, exc = numBottles, numExchange

        while bot >= exc:
            bot -= exc
            exc += 1
            ans += 1
            bot += 1

        return ans
