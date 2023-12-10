class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        
        i, j, count, ans = 0, 0, 0, 0
        
        while(j < n):
            if(nums[j] == mx):
                count += 1
            if(count >= k):
                while(count >= k):
                    ans += (n - j)
                
                    if(nums[i] == mx):
                        count -= 1
                    i += 1
                    
            j += 1
            
        return ans