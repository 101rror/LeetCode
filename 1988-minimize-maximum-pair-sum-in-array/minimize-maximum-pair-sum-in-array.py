class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        maxsum = 0
        for i in range(n // 2):
            maxsum = max(maxsum, nums[i] + nums[n - i - 1])

        return maxsum
