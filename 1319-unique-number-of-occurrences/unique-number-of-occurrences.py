class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = defaultdict(int)
        st = set()

        for num in arr:
            mp[num] += 1

        st = set(mp.values())

        x = len(mp.values())
        y = len(st)

        return x == y
