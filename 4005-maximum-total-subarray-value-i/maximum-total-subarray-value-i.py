class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mn = mx = nums[0]

        for num in nums:
            mn = min(mn, num)
            mx = max(mx, num)

        return (mx - mn) * k
