class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf] * (k - 1) + [0]
        pre, ans = 0, -inf

        for key, val in enumerate(nums):
            pre += val
            nk = key % k
            ans = max(ans, pre - dp[nk])
            dp[nk] = min(pre, dp[nk])

        return ans
