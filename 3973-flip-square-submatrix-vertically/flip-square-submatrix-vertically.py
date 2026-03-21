# Added using AI
class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        sc, ec = y, y + k - 1
        sr = x
        
        for j in range(sc, ec + 1):
            for i in range(k // 2):
                grid[sr + i][j], grid[sr + k - i - 1][j] = (grid[sr + k - i - 1][j], grid[sr + i][j])

        return grid
