class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        tsum = 0

        for i in range(0, n):
            if(i % 2 == 0):
                tsum += nums[i]
            else:
                continue

        return tsum
        