class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        for i in range(n // 2):
            x = nums[i] + nums[n - i - 1]
            ans = max(ans, x)

        return ans
