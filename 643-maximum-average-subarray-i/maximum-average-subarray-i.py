class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ksum = sum(nums[0 : k])
        maxsum = ksum
        j = 0

        for i in range(k, n):
            ksum -= nums[j]
            ksum += nums[i]
            maxsum = max(maxsum, ksum)
            j += 1

        return maxsum / k