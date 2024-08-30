class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count, lo, n = 0, -1, len(colors)

        for hi in range(1, n + k - 1):
            if colors[hi % n] == colors[(hi - 1) % n]:
                lo = hi - 1
            elif hi - lo >= k:
                count += 1

        return count