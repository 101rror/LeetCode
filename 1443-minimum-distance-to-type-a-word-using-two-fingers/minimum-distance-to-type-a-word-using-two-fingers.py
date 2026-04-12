from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        def dist(a, b):
            if a == 26 or b == 26:
                return 0

            row1, col1 = divmod(a, 6)
            row2, col2 = divmod(b, 6)

            return abs(row1 - row2) + abs(col1 - col2)

        @lru_cache(None)
        def solve(idx, f1, f2):
            if idx == n:
                return 0

            cur = ord(word[idx]) - ord("A")

            x = dist(f1, cur) + solve(idx + 1, cur, f2)
            y = dist(f2, cur) + solve(idx + 1, f1, cur)

            return min(x, y)

        return solve(0, 26, 26)
