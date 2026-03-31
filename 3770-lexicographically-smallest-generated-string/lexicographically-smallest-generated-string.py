class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        s = ["a"] * (n + m - 1)
        dp = [False] * (n + m - 1)

        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if dp[j] and s[j] != c:
                        return ""
                    s[j], dp[j] = c, True

        for i, ch in enumerate(str1):
            if ch == "F":
                if any(str2[j - i] != s[j] for j in range(i, i + m)):
                    continue

                for j in range(i + m - 1, i - 1, -1):
                    if not dp[j]:
                        s[j] = "b"
                        break
                else:
                    return ""

        return "".join(s)
