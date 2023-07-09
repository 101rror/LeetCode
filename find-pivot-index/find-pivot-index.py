class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        Leftsum = 0
        Rightsum = sum(nums)
        
        for i in range(n):
            if(Leftsum == Rightsum - nums[i]):
                return i
                
            Leftsum += nums[i]
            Rightsum -= nums[i]
            
        return -1