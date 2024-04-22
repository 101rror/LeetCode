class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = []
        upper = []
        special = 0

        for i in word:
            if i >= 'a' and i <= 'z':
                lower.append(i.upper())
            else:
                upper.append(i)

        special = set(lower) & set(upper)

        return len(special)