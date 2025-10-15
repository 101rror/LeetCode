class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        inc, preinc, ans = 1, 0, 0

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc += 1
            else:
                preinc = inc
                inc = 1

            half = inc >> 1
            mn = min(preinc, inc)
            maxc = max(half, mn)
            ans = max(ans, maxc)

        return ans
