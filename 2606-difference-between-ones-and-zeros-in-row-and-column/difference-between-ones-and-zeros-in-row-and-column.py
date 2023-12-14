class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        def tsum(nums) : 
            return 2 * sum(nums) - len(nums)

        r, c = len(grid), len(grid[0])
            
        rows = list(map(tsum, grid))
        cols = list(map(tsum, zip(*grid)))
        
        for i, j in product(range(r), range(c)):
            grid[i][j] = rows[i] + cols[j]

        return grid