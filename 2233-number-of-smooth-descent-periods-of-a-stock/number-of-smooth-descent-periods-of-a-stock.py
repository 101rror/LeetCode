class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, count = 0, 0
        prev = -math.inf

        for curr in prices:
            if prev - curr == 1:
                count += 1
            else:
                count = 1
            ans += count
            prev = curr

        return ans
