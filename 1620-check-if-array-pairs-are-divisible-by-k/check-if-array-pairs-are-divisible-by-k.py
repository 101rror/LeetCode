class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter()

        for div in arr:
            counter[div % k] += 1

        if counter[0] % 2 != 0:
            return False

        for key, value in counter.items():
            if key > 0 and counter[k - key] != value:
                return False

        return True