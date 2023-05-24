class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high - low)

        if(low % 2 == 0) and (high % 2 == 0):
            return ans // 2

        if(low % 2 != 0) or (high % 2 != 0):
            return ans // 2 + 1