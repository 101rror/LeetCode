class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        mx = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    curr = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                    mx = max(mx, curr)
                    
        return mx / 2