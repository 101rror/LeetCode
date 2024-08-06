from collections import defaultdict

class Solution:
    def minimumPushes(self, word: str) -> int:
        map = defaultdict(int)

        for i in word:
            map[i] += 1

        values = sorted(map.values(), reverse=True)
        n = len(values)

        tsum = 0

        for i in range(1, n + 1):
            if i <= 8:
                tsum += values[i - 1]
            elif 8 < i <= 16:
                tsum += values[i - 1] * 2
            elif 16 < i <= 24:
                tsum += values[i - 1] * 3
            elif 24 < i:
                tsum += values[i - 1] * 4

        return tsum