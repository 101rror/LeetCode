class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        if n % 2 == 0:
            c = list(s[: int(n / 2)])
            c.sort()
            x = "".join(c)
            return x + x[::-1]

        else:
            m = s[int((n + 1) / 2) - 1]
            c = list(s[: int((n - 1) / 2)])
            c.sort()
            x = "".join(c)
            return x + m + x[::-1]

        return 0
