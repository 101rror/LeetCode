class Solution:
    def minTime(self, skills: List[int], energy: List[int]) -> int:
        n, m = len(skills), len(energy)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = dp[i - 1] + skills[i]

        ans = skills[0] * energy[0]

        for j in range(1, m):
            mx = skills[0] * energy[j]
            for i in range(1, n):
                dif = dp[i] * energy[j - 1] - dp[i - 1] * energy[j]
                if dif > mx:
                    mx = dif
            ans += mx

        return ans + dp[-1] * energy[-1]
