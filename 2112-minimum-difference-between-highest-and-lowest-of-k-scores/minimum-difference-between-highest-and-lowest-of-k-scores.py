class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mn = float("inf")

        for i in range(n - k + 1):
            cur = nums[i + k - 1] - nums[i]
            mn = min(mn, cur)

        return mn
