class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        mn = float('inf')
        
        for i in range(l, r + 1):
            cur = sum(nums[:i])
            if cur > 0:
                mn = min(mn, cur)
                
            for j in range(i, n):
                cur += nums[j] - nums[j - i]
                if cur > 0:
                    mn = min(mn, cur)
                    
        return mn if mn != float('inf') else -1