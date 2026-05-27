class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower[ch] = i
            else:
                if ch.lower() not in upper:
                    upper[ch.lower()] = i

        count = 0

        for ch in lower:
            if ch in upper and lower[ch] < upper[ch]:
                count += 1

        return count
