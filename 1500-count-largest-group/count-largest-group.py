class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = Counter()

        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            counter[key] += 1

        mx = max(counter.values())
        count = 0

        for val in counter.values():
            if val == mx:
                count += 1

        return count
