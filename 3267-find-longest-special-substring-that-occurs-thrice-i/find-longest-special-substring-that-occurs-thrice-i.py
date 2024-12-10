class Solution:
    def maximumLength(self, s: str) -> int:
        dct = defaultdict(int)
        subs = ["".join(sub) for _, sub in groupby(s)]

        for sub in subs:
            dct[sub] += 1
            if len(sub) > 1:
                dct[sub[1:]] += 2
            if len(sub) > 2:
                dct[sub[2:]] += 3

        return max(map(len, filter(lambda x: dct[x] > 2, dct)), default=-1)