class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minL, minW, ans = 3000, 3000, 3000
        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            minL = min(minL, landStartTime[i] + landDuration[i])

        for i in range(m):
            minW = min(minW, waterStartTime[i] + waterDuration[i])
            ans = min(ans, max(minL, waterStartTime[i]) + waterDuration[i])

        for i in range(n):
            ans = min(ans, max(minW, landStartTime[i]) + landDuration[i])

        return ans
