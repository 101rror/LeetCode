class Solution:
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        seen = set()
        left, curSum, maxSum = 0, 0, 0

        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                curSum -= nums[left]
                left += 1
                
            seen.add(nums[right])
            curSum += nums[right]
            maxSum = max(maxSum, curSum)

        return maxSum
