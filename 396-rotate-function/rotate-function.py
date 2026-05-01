class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        tSum = sum(nums)
        mx = 0

        for i in range(n):
            mx += (nums[i] * i)

        curr = mx

        for i in range(1, n):
            curr += tSum - n * nums[n - i]
            mx = max(mx, curr)

        return mx
