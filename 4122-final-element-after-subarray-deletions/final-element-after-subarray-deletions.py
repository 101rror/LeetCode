class Solution:
    def finalElement(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums[0], nums[n - 1])
