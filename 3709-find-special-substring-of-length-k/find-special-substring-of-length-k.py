class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        last = 0

        for first in range(n):
            if s[first] != s[last]:
                if first - last == k:
                    return True
                last = first

        return n - last == k
