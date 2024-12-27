class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        values = list(counter.values())

        for i in range(1, len(values)):
            if values[i] != values[i - 1]:
                return False

        return True