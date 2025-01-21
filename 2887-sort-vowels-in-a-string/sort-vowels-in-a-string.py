VOWELS = "AEIOUaeiou"

TRANS = str.maketrans(VOWELS, "_" * 10)

class Solution:
    def sortVowels(self, s: str) -> str:
        s2 = s.translate(TRANS)

        for vowel in VOWELS:
            s2 = s2.replace("_", vowel, s.count(vowel))

        return s2