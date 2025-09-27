class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

        preSum = [(0, 0)] * (n + 1)
        ans = set()

        for i in range(n):
            dx, dy = move[s[i]]
            px, py = preSum[i]
            preSum[i + 1] = (px + dx, py + dy)

        tx, ty = preSum[n]

        for i in range(n - k + 1):
            px, py = preSum[i]
            rx1, ry1 = preSum[i + k]
            rx0, ry0 = preSum[i]

            rdx, rdy = rx1 - rx0, ry1 - ry0
            ans.add((tx - rdx, ty - rdy))

        return len(ans)
