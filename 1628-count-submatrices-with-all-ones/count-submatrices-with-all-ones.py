class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [0] * n
        count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    dp[j] += 1
                else:
                    dp[j] = 0

            for j in range(n):
                mn, k = dp[j], j
                while k >= 0 and mn:
                    mn = min(mn, dp[k])
                    count += mn
                    k -= 1

        return count
