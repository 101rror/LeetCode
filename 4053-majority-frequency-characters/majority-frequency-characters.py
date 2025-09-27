class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)
        groups = defaultdict(list)

        for ch, f in freq.items():
            groups[f].append(ch)

        mx, bk = -1, -1
        for k, chars in groups.items():
            n = len(chars)
            if n > mx or (n == mx and k > bk):
                mx, bk = n, k

        return "".join(groups[bk])
