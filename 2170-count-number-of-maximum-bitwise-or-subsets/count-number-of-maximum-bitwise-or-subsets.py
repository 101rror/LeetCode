class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxval = 0
        dp = [0] * (1 << 17)

        dp[0] = 1

        for num in nums:
            for i in range(maxval, -1, -1):
                dp[i | num] += dp[i]

            maxval |= num

        return dp[maxval]