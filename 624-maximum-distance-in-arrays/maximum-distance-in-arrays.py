class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        low1 = 10000
        high1 = -10000
        low2 = 10000
        high2 = -10000
        lowindex = 0
        highindex = 0

        for i in range(len(arrays)):
            mn = min(arrays[i])
            
            if mn < low1:
                low1 = mn
                lowindex = i

        for i in range(len(arrays)):
            mx = max(arrays[i])
            
            if i != lowindex and mx > high1:
                high1 = mx

        for i in range(len(arrays)):
            mx = max(arrays[i])
            
            if mx > high2:
                high2 = mx
                highindex = i

        for i in range(len(arrays)):
            mn = min(arrays[i])
            
            if i != highindex and mn < low2:
                low2 = mn

        low = (high1 - low1)
        high = (high2 - low2)

        ans = max(low, high)

        return ans