class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        mx = 0

        for i in range(n):
            ai, bi = bottomLeft[i]
            ci, di = topRight[i]
            for j in range(i + 1, n):
                aj, bj = bottomLeft[j]
                cj, dj = topRight[j]

                height = min(cj, ci) - max(aj, ai)
                width = min(dj, di) - max(bj, bi)

                mn = min(height, width)
                mx = max(mx, mn)

        return pow(mx, 2)
