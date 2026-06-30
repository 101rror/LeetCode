class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        idx = [0] * 3
        count = 0

        for i, c in enumerate(s, 1):
            idx[ord(c) - ord("a")] = i
            count += min(idx)

        return count
