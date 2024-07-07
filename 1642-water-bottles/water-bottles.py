class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        div = ((numBottles - 1) // (numExchange - 1))
        ans = numBottles + div

        return ans