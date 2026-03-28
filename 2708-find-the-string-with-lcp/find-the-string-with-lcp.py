class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""

        res = [""] * n
        curc = "a"

        for i in range(n):
            if res[i] == "":
                if curc > "z":
                    return ""

                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = curc

                curc = chr(ord(curc) + 1)

        word = "".join(res)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0

                if dp[i][j] != lcp[i][j]:
                    return ""

        return word
