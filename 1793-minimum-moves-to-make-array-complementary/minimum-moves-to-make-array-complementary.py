class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        dp = [0] * (2 * limit + 2)

        for i in range(n // 2):
            mn = min(nums[i], nums[-1 - i])
            mx = max(nums[i], nums[-1 - i])

            dp[2] += 2
            dp[mn + 1] -= 1
            dp[mn + mx] -= 1
            dp[mn + mx + 1] += 1
            dp[mx + limit + 1] += 1

        ans, moves = n, 0

        for tar in range(2, 2 * limit + 1):
            moves += dp[tar]
            ans = min(ans, moves)

        return ans
