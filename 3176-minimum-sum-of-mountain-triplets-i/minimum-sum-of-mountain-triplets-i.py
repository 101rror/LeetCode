class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mn = 10000
        flag = False
        
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if((nums[i] < nums[j] and nums[k] < nums[j]) and (i < j and j < k)):
                        ans = (nums[i] + nums[j] + nums[k])
                        
                        if(ans < mn):
                            mn = ans
                            flag = True
                        
                    
        if(flag):
            return mn
        else:
            return -1