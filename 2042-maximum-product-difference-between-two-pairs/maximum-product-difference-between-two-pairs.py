class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        a = nums[0]
        b = nums[1]
        c = nums[n - 1]
        d = nums[n - 2]

        ans = ((c * d) - (a * b))

        return ans