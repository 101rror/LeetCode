class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()

        while pq:
            mx, r, c = heapq.heappop(pq)
            if (r, c) in seen:
                continue
            seen.add((r, c))

            if r == m - 1 and c == n - 1:
                return mx

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    mxx = max(mx, grid[nr][nc])
                    heapq.heappush(pq, (mxx, nr, nc))

        return -1
