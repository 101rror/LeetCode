class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10 ** 9 + 7
        seen, mx = set(), 0
        hFences = sorted(chain(hFences, [1, m]))
        vFences = sorted(chain(vFences, [1, n]))

        for i, top in enumerate(hFences):
            for bot in hFences[i + 1 :]:
                seen.add(bot - top)

        for i, lft in enumerate(vFences):
            for rgt in vFences[i + 1 :][::-1]:
                x = rgt - lft
                if x <= mx or x not in seen:
                    continue
                mx = x
                break

        if mx == 0:
            return -1
            
        return pow(mx, 2, MOD)
