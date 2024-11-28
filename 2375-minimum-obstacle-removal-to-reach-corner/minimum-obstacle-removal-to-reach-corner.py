class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0, 0)])
        
        while dq:
            o, r, c = dq.popleft()
            for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if m > i >= 0 <= j < n and dist[i][j] == inf:
                    if grid[i][j] == 1:
                        dist[i][j] = o + 1
                        dq.append((o + 1, i, j))
                    else:
                        dist[i][j] = o
                        dq.appendleft((o, i, j))    

        return dist[-1][-1]