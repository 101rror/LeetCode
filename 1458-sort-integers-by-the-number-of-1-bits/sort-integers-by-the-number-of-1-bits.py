class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        mp = defaultdict(list)

        for num in arr:
            mp[bin(num).count("1")].append(num)

        ans = []

        for k in sorted(mp.keys()):
            for i in sorted(mp[k]):
                ans.append(i)

        return ans
