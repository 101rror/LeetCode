class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        subsum = 0
        maxsum = 0

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                subsum += nums[i - 1]
            else:
                subsum += nums[i - 1]
                maxsum = max(maxsum, subsum)
                subsum = 0

        subsum += nums[n - 1]

        maxsum = max(maxsum, subsum)
        return maxsum
