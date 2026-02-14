class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(query_row + 1)]
        dp[0][0] = poured

        for row in range(query_row):
            for glass in range(len(dp[row])):
                excess = (dp[row][glass] - 1) / 2
                if excess > 0:
                    dp[row + 1][glass] += excess
                    dp[row + 1][glass + 1] += excess

        return min(1, dp[query_row][query_glass])
