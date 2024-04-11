class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        tsum = nums[0]
        
        for i in range(1, len(nums)):
            if(nums[i - 1] + 1 == nums[i]):
                tsum += nums[i]
            else:
                break
        
        while True:
            if tsum not in nums:
                return tsum
            else:
                tsum += 1