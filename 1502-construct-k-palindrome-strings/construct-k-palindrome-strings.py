class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        counter = Counter(s)
        odd = 0

        for key, val in counter.items():
            if val % 2 != 0:
                odd += 1

        return odd <= k