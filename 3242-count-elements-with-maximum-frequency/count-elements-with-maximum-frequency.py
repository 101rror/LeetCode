class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = []
        
        for i in nums:
            mp[i] += 1
            
        for i in mp.values():
            ans.append(i)
            
        ans = sorted(ans, reverse = True)
        
        if(ans[0] == 1):
            return sum(ans)
        else:
            mx = ans[0]
            tsum = 0
            for i in ans:
                if(i == mx):
                    tsum += i
                    
            return tsum