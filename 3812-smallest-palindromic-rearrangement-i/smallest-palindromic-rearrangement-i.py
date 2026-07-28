class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half = "".join(sorted(s[: n // 2]))

        if n % 2:
            return half + s[n // 2] + half[::-1]

        return half + half[::-1]
