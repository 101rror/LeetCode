class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        counter = Counter(s)
        remove = 0

        for key, val in counter.items():
            if val > 2 and val % 2 == 1:
                remove += val - 1
            elif val > 2 and val % 2 == 0:
                remove += val - 2

        return n - remove
