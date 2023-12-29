class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        
        @lru_cache(None)
        def dp(idx, d, curr):
            if idx == len(job) and d == 0:
                return curr
            if idx >= len(job) or  d <= 0:
                return inf
            
            return min(dp(idx + 1, d, max(curr, job[idx])),
                       max(curr, job[idx]) + dp(idx + 1, d - 1, 0))
       
        ans = dp(0, d, 0)

        if ans != inf:
            return ans 
        else:
            return -1