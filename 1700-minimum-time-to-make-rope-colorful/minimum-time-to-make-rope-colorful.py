class Solution:
    def minCost(self, co: str, tm: List[int]) -> int:
        n = len(co)
        tsum, pre = 0, 0

        for i in range(1, n):
            if(co[pre] != co[i]):
                pre = i
            else:
                tsum += min(tm[pre], tm[i])
                if(tm[pre] < tm[i]):
                    pre = i

        return tsum