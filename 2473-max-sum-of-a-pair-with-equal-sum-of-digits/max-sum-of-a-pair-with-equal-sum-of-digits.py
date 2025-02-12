class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dp = [0] * 82
        ans = -1

        for x in nums:
            dsum = sum(int(d) for d in str(x))
            if dp[dsum] != 0:
                ans = max(ans, x + dp[dsum])
            dp[dsum] = max(dp[dsum], x)

        return ans
