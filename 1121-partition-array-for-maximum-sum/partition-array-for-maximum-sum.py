class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        if(n == 1 or k == 1):
            return sum(arr)
        elif(n == k):
            return max(arr) * n
        else:
            dp = [0]*n

            for i in range(k):
                dp[i] = max(arr[: i + 1]) * (i + 1)

            for i in range(k, n):
                cur = []
                for j in range(k):
                    cur.append(dp[i - j - 1] + max(arr[(i - j) : (i + 1)]) * (j + 1))
                dp[i] = max(cur)

            return dp[-1]           