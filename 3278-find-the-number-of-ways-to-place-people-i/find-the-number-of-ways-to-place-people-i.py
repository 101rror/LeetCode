class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        pairs = 0
        n = len(points)

        for i in range(n):
            uppy = points[i][1]
            lowy = float("-inf")
            for j in range(i + 1, n):
                cury = points[j][1]
                if cury <= uppy and cury > lowy:
                    pairs += 1
                    lowy = cury
                    if cury == uppy:
                        break

        return pairs
