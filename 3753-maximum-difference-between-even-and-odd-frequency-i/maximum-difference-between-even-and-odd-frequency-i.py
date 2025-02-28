class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        mx = -maxsize
        mn = maxsize

        for freq in counter.values():
            if freq & 1:
                mx = max(mx, freq)
            else:
                mn = min(mn, freq)

        return mx - mn
