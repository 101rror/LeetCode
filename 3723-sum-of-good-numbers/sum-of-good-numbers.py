class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        n = len(nums)
        Gsum = 0

        for i, num in enumerate(nums):
            if i - k >= 0 and num <= nums[i - k]:
                continue
            if i + k < n and num <= nums[i + k]:
                continue
            Gsum += num

        return Gsum
