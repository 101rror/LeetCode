class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tsum = 0
        
        for i in range(n):
            x = bin(i).count("1")
            if(x == k):
                tsum += nums[i]
                
        return tsum