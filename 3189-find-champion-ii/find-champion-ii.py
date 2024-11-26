class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        count = 0
        dp = [0] * n

        for edge in edges:
            dp[edge[1]] += 1

        champion = -1

        for i in range(n):
            if dp[i] == 0:
                count += 1
                champion = i

        return champion if count == 1 else -1