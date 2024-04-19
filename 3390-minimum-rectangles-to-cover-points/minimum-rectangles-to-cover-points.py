class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = i = j = 0

        while j < len(points):
            if points[j][0] - points[i][0] > w:
                ans += 1
                i = j
            j += 1

        return ans + 1