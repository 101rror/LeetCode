class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        new = [
            len(row) - 1 - max((i for i, v in enumerate(row) if v), default=-1)
            for row in grid
        ]

        ans = 0
        for i in range(n):
            need = n - i - 1
            j = i
            while j < n and new[j] < need:
                j += 1
            if j == n:
                return -1
            ans += j - i
            new[i : j + 1] = new[j : j + 1] + new[i:j]

        return ans
