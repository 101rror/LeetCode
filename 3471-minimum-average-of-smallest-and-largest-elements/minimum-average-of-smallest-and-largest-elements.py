class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        ans = []
        
        while nums:
            mn = nums.pop(0)
            mx = nums.pop(-1)
            
            avg = (mn + mx) / 2
            
            ans.append(avg)
            
        return min(ans)