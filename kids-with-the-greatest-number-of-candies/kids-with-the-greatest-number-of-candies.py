class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        m = max(candies)
        ans = []
        count = 0

        for i in range(n):
            count = candies[i] + extraCandies
            if(count >= m):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans