class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        mx = nums[-1] * nums[-2] * nums[-3]
        mn = nums[-1] * nums[0] * nums[1]

        return max(mx, mn)
