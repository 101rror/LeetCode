class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        zero = 1

        for i in range(n):
            zero -= nums[i] == 0
            if(zero < 0):
                zero += nums[l] == 0
                l += 1

        return i - l