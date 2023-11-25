class Solution:
    def getSumAbsoluteDifferences(self, nums):
        nsum, tsum, n = 0, sum(nums), len(nums)
        ans = []

        for i in range(0, n):
            ans.append(tsum - nums[i] * (n - i) + nums[i] * i - nsum)
            tsum -= nums[i]
            nsum += nums[i]

        return ans