class Solution:
    def largestGoodInteger(self, s: str) -> str:
        ans = ""
        n = len(s)

        for i in range(n - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                ans = max(ans, s[i : i + 3])

        return ans
