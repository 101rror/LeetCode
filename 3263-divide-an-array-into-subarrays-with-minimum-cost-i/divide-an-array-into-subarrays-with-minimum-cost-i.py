class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        nums.pop(0)
        nums.sort()
        first += nums[0] + nums[1]

        return first
