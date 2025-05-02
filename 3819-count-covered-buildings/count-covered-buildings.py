class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cm = [n + 1] * (n + 1)
        cM = [0] * (n + 1)
        rm = [n + 1] * (n + 1)
        rM = [0] * (n + 1)

        for x, y in buildings:
            cm[x] = min(cm[x], y)
            cM[x] = max(cM[x], y)
            rm[y] = min(rm[y], x)
            rM[y] = max(rM[y], x)

        count = 0

        for x, y in buildings:
            if cm[x] < y < cM[x] and rm[y] < x < rM[y]:
                count += 1

        return count
