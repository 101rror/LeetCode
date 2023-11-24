class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles = sorted(piles, reverse = True)
        ans = []
        mx = 0

        fi = 0
        la = n - 1

        while(fi <= la):
            ans.append(piles[fi])
            ans.append(piles[fi + 1])

            fi += 2
            la -= 1

        ans.sort()

        for i in range(0, len(ans), 2):
            mx += ans[i]

        return mx