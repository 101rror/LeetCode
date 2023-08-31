class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums, reverse = True)

        x = (nums[0] - 1)
        y = (nums[1] - 1)

        ans = (x * y)

        return ans