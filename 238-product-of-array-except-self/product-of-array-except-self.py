import math as mt

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        mul = 1

        for i in nums:
            mul *= i
            
        for i in range(n):
            if(nums[i] == 0):
                ans.append(mt.prod(nums[:i] + nums[i + 1:]))
            else: 
                ans.append(int(mul/nums[i]))

        return ans