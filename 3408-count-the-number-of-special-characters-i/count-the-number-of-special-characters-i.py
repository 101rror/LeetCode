class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        seen = set()
        for ch in word:
            if ch not in seen and ch.islower():
                if ch.upper() in word:
                    count += 1

            seen.add(ch)

        return count
