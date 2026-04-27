from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        streets = {1: [0, 1], 2: [2, 3], 3: [0, 3], 4: [1, 3], 5: [0, 2], 6: [1, 2]}

        opposite = {0: 1, 1: 0, 2: 3, 3: 2}

        visited = [[False] * n for _ in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = True

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for d in streets[grid[r][c]]:
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]

                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue

                next = grid[nr][nc]

                if opposite[d] in streets[next]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

        return False
