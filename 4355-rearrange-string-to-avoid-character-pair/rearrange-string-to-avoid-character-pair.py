class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = ""

        for c in s:
            if c == y:
                ans += c
        for c in s:
            if c != x and c != y:
                ans += c
        for c in s:
            if c == x:
                ans += c

        return ans
