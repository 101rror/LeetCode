class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        first = 1
        last = max(piles)
        
        while (first < last):
            mid = (first + last) // 2
            hours = 0
            
            for i in piles:
                hours += ceil(i / mid)
                
            if hours <= h:
                last = mid

            else:
                first = mid + 1
            
        return last