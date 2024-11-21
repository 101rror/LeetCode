class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for x, y in guards:
            dp[x][y] = 3  
        for x, y in walls:
            dp[x][y] = 3

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for gx, gy in guards:
            for dx, dy in dirs:
                x, y = gx, gy

                while True:
                    x += dx
                    y += dy

                    if x < 0 or y < 0 or x >= m or y >= n or dp[x][y] == 3:
                        break

                    dp[x][y] = 1

        ans = 0
        for arr in dp:
            zero = arr.count(0)
            ans += zero

        return ans