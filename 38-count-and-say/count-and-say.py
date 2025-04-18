class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            res = self.describe(res)
        return res

    def describe(self, s: str) -> str:
        ans = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                ans.append(f"{count}{s[i - 1]}")
                count = 1

        ans.append(f"{count}{s[-1]}")

        return "".join(ans)
