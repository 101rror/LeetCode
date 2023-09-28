class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        mn = min(nums)
        count = 0
        a = []
        b = []
        srt = sorted(nums)
        
        if(srt == nums):
            return 0
        
        for i in range(n):
            if(nums[i] != mn):
                a.append(nums[i])
            if(nums[i] == mn):
                break
                
        nums.reverse()
                
        for i in range(n):
            if(nums[i] != mn):
                b.append(nums[i])
            if(nums[i] == mn):
                break
        b.append(mn)
        b.reverse()
        
        ans = len(b)
        
        for i in range(len(a)):
            b.append(a[i])
        
        if(b == srt):
            return ans
        else:
            return -1
                