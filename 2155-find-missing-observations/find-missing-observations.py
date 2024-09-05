class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ln = len(rolls)
        ans = []

        tsum = mean * (n + ln)
        misssum = tsum - sum(rolls)

        if misssum > 6 * n or misssum < n:
            return ans

        while n:
            curr = min(6, misssum - n + 1)
            ans.append(curr)
            misssum -= curr
            n -= 1

        return ans
        