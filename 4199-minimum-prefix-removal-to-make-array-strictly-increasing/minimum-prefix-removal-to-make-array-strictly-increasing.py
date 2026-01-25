class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        n -= 1

        while n > 0 and nums[n - 1] < nums[n]:
            n -= 1

        return n
