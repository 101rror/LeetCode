class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        it = 1

        while it < len(s):
            if s[it - 1] != s[it]:
                count += 1

            it += 2

        return count