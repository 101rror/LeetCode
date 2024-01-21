class Solution:
    def rob(self, nums: List[int]) -> int:
        mx = nums[0]
        x = 0
        if len(nums) <= 2:
            return max(nums)

        for i in range(1, len(nums)):
            temp = mx
            mx = max(mx, nums[i] + x)
            x = temp

        return mx