class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        lst = [{"N", "E"}, {"N", "W"}, {"S", "E"}, {"S", "W"}]
        ans = 0

        for diag in lst:
            kk, dist = k, 0
            for ch in s:
                if ch in diag or kk:
                    dist += 1
                    kk -= ch not in diag
                else:
                    dist -= 1
                ans = max(ans, dist)

        return ans
