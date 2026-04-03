class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        comb = []
        
        for i in range(n):
            comb.append((robots[i], distance[i]))

        comb.sort()
        walls.sort()

        def count(L, R):
            l = bisect.bisect_left(walls, L)
            r = bisect.bisect_right(walls, R)
            return r - l

        @cache
        def recursive(i, last):
            if i == n:
                return 0
            pos, dis = comb[i]

            l = max(pos - dis, comb[i - 1][0] + 1) if i else pos - dis
            r = min(pos + dis, comb[i + 1][0] - 1) if i < n - 1 else pos + dis

            lcount = count(l, pos)
            rcount = count(pos, r)

            if last:
                lcount = count(max(pos - dis, comb[i - 1][0] + comb[i - 1][1] + 1), pos)

            return max(lcount + recursive(i + 1, 0), rcount + recursive(i + 1, 1))

        return recursive(0, 0)
