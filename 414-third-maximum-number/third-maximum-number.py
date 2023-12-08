class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        def unique(arr):
            ans = []
            for i in arr:
                if i not in ans:
                    ans.append(i)
                    
            return ans
                
        ans = unique(nums)
        
        ans = sorted(ans, reverse = True)
        
        if(len(ans) < 3):
            return max(ans)
        
        return ans[2]