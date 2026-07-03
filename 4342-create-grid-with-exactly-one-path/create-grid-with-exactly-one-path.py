class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = [["." for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(n - 1):
                grid[i][j] = "#"

        return ["".join(row) for row in grid]
