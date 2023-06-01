class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if(grid[0][0] != 0 or grid[-1][-1] != 0):
            return -1

        len1 = len(grid)
        len2 = len(grid[0])
        q = [(0, 0, 1)]

        while (len(q) > 0):
            x, y, z = q.pop(0)

            if(x == len1 - 1 and y == len2 - 1):
                return z
            for a, b in ((x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1)):
                if(0 <= a < len1 and 0 <= b < len2 and grid[a][b] == 0):
                    grid[a][b] = 1
                    q.append((a, b, z + 1))

        return -1