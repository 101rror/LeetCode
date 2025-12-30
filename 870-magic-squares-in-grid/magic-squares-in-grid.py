class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0

        square = [
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        ]

        if n < 3 or m < 3:
            return 0

        for row in range(n - 2):
            for col in range(m - 2):
                sub = [grid[row + i][col : col + 3] for i in range(3)]

                if sub in square:
                    count += 1

        return count
