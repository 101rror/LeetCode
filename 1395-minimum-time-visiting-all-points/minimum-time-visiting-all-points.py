class Solution:
    def minTimeToVisitAllPoints(self, points):
        ans = 0
        n = len(points)

        for i in range(1, n):
            difx = abs(points[i][0] - points[i - 1][0])
            dify = abs(points[i][1] - points[i - 1][1])
            ans += max(difx, dify)

        return ans
