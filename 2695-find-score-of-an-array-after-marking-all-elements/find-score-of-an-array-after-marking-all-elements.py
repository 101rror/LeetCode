class Solution:
    def findScore(self, nums: List[int]) -> int:

        n, ans, seen = len(nums), 0, set()

        queue = sorted(enumerate(nums), key = lambda x: (x[1],x[0]))

        for idx, num in queue:
            if idx in seen:
                continue

            ans += num
            
            seen.add(idx)

            if idx > 0  :
                seen.add(idx-1)
            if idx < n-1:
                seen.add(idx+1) 
            
        return ans