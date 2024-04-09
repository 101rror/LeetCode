class Solution:
    def timeRequiredToBuy(self, tkt: List[int], k: int) -> int:
        tsum = 0

        for i, x in enumerate(tkt):
            if i <= k:
                tsum += min(tkt[i], tkt[k])
            else:
                tsum += min(tkt[i], tkt[k] - 1)

        return tsum