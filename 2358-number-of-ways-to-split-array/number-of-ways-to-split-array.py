class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        prefixsum = [0] * n
        prefixsum[0] = nums[0]

        for i in range(1, n):
            prefixsum[i] = prefixsum[i - 1] + nums[i]

        for i in range(n - 1):
            if prefixsum[i] >= prefixsum[-1] - prefixsum[i]:
                count += 1

        return count
