class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0

        for i in range(len(grid[0])):
            ans = []
            for j in range(len(grid)):
                ans.append(grid[j][i])

            for i in range(len(grid)):
                if ans == grid[i]:
                    count += 1

        return count