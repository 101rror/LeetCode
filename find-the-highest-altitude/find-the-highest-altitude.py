class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        ans = []
        ans.append(0)

        for i in range(0, n):
            check = (ans[i] + gain[i])

            ans.append(check)

        mx = max(ans)

        return mx