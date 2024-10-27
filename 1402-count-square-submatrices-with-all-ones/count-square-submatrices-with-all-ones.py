class Solution(object):
    def countSquares(self, matrix):
        n1, n2 = len(matrix), len(matrix[0])
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        ans = 0

        for i in range(n1):
            for j in range(n2):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    ans += dp[i + 1][j + 1]
                    
        return ans