class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: (x[0], -x[1]))
        ans = r = 0

        for st, end in A:
            ans += end > r
            r = max(r, end)

        return ans
