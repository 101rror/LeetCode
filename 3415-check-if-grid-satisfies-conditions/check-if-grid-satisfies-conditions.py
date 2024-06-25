class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for a, b in pairwise(grid[0]):
            if a == b:
                return False

        for s in list(map(set, zip(*grid))): 
            if len(s) != 1:
                return False

        return True