class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        
        if(n <= 2):
            return -1
        else:
            return nums[1]