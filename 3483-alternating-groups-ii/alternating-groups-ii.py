class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        count = 0
        left = 0

        for right in range(1, n + k - 1):
            if colors[right % n] == colors[(right - 1) % n]:
                left = right
            if right - left + 1 >= k:
                count += 1

        return count
