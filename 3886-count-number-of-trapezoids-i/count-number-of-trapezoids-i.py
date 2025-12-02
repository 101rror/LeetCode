class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        mp = defaultdict(int)
        for _, y in points:
            mp[y] += 1

        ans = tot = 0

        for y, count in mp.items():
            li = count * (count - 1) // 2
            ans = (ans + tot * li)
            tot = (tot + li)

        return ans % MOD