class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        else:
            tsum = nums[0]
            nums.pop(0)
            nums.sort()
            tsum += nums[0] + nums[1]
            
            return tsum
            