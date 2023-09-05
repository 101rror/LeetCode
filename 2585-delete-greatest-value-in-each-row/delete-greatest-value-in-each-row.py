class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = []

        while (len(grid[0]) > 0):
            s = []

            for i in grid:
                mx = max(i)
                i.remove(mx)
                s.append(mx)
            ans.append(max(s))
            
        return sum(ans)