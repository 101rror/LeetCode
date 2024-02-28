class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        
        for i in nums:
            mp[i] += 1
            
        for i in mp.values():
            if i > 2:
                return False
            
        return True