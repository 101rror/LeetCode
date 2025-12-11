class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        colMin = [n + 1] * (n + 1)
        colMax = [0] * (n + 1)
        rowMin = [n + 1] * (n + 1)
        rowMax = [0] * (n + 1)

        for x, y in buildings:
            colMin[x] = min(colMin[x], y)
            colMax[x] = max(colMax[x], y)
            rowMin[y] = min(rowMin[y], x)
            rowMax[y] = max(rowMax[y], x)

        for x, y in buildings:
            if colMin[x] < y < colMax[x] and rowMin[y] < x < rowMax[y]:
                count += 1

        return count
