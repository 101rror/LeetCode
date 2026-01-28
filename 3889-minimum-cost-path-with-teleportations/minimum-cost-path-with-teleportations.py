class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        flat = []
        available = []

        for i in range(rows):
            for j in range(cols):
                flat.append((grid[i][j], i, j))

        flat.sort(reverse=True)

        for _ in range(k):
            available.append(flat.copy())

        heap = [(0, 0, 0, 0)]
        vis = []

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(11)
            vis.append(row)

        while heap:
            cost, x, y, tps = heapq.heappop(heap)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return cost
            if vis[x][y] <= tps:
                continue
            vis[x][y] = tps
            if x + 1 < len(grid):
                heapq.heappush(heap, (cost + grid[x + 1][y], x + 1, y, tps))
            if y + 1 < len(grid[0]):
                heapq.heappush(heap, (cost + grid[x][y + 1], x, y + 1, tps))

            while tps < k and available[tps] and available[tps][-1][0] <= grid[x][y]:
                c1, x1, y1 = available[tps].pop()
                heapq.heappush(heap, (cost, x1, y1, tps + 1))
