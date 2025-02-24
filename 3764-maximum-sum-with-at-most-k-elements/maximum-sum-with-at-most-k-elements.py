class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        a = []

        for i in range(len(grid)):
            s = sorted(grid[i], reverse=True)

            a.extend(s[: limits[i]])

        a.sort()
        s = 0

        for i in range(k):
            s += a.pop()

        return s
