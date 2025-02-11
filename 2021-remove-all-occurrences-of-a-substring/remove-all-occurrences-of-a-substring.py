class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        plen = len(part)

        while part in s:
            idx = s.find(part)
            s = s[:idx] + s[idx + plen :]

        return s
