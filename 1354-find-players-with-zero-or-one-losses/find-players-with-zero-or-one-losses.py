class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        ans1 = []
        ans2 = []

        for i in m:
            mp[i[0]] += 0
            mp[i[1]] += 1

        for key, value in mp.items():
            if value == 0:
                ans1.append(key)

        for key, value in mp.items():
            if value == 1:
                ans2.append(key)

        ans1.sort()
        ans2.sort()

        return [ans1, ans2]