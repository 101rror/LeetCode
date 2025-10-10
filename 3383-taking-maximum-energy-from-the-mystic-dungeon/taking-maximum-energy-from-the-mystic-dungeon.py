class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float("-inf")
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]

            ans = max(ans, dp[i])

        return ans
