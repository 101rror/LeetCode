class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        dp = [0] * n
        ans = []

        for i in range(1, n):
            dp[i] = dp[i - 1]
            if (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0) or (
                nums[i - 1] % 2 != 0 and nums[i] % 2 != 0
            ):
                dp[i] += 1

        for left, right in queries:
            count = dp[right] - (dp[left] if left > 0 else 0)
            ans.append(count == 0)

        return ans
