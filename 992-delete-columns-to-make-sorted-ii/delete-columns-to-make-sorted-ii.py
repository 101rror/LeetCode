class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row, col = len(strs), len(strs[0])
        ans, dp = 0, [False] * (row - 1)

        for j in range(col):
            temp = dp[:]
            for i in range(row - 1):
                if not dp[i] and strs[i][j] > strs[i + 1][j]:
                    ans += 1
                    break
                elif strs[i][j] < strs[i + 1][j] and not dp[i]:
                    temp[i] = True
            else:
                dp = temp
            if all(dp):
                return ans

        return ans
