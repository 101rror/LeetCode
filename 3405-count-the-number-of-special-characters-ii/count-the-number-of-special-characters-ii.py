class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        count = 0

        for i in range(n):
            x = word[i]
            if x.isupper():
                bsub = word[0 : i]
                fsub = word[i + 1 : n + 1]

                if x.lower() in bsub and x.lower() not in fsub and x.upper() not in bsub:
                    count += 1

        return count
