class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = nums[len(nums) // 2]

        return nums.count(mid) == 1
