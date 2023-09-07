class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        ans = heights
        count = 0

        ans = sorted(ans)

        for i in range(n):
            if(ans[i] != heights[i]):
                count += 1
        
        return count
        