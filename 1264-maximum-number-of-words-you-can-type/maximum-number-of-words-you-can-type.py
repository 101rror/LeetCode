class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        keySet = set(broken)
        words = text.split(" ")
        count = 0

        for word in words:
            for c in word:
                if c in keySet:
                    count += 1
                    break

        return len(words) - count
