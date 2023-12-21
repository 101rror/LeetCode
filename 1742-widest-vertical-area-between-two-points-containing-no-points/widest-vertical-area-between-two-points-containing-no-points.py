class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        mx = 0

        for i in range(n - 1):
            x = points[i + 1][0] - points[i][0]
            if x > mx:
                mx = x
                
        return mx