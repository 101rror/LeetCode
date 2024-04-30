class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for si in range(2):
            for sj in range(2):
                nb = 0
                for i in range(2):
                    for j in range(2):
                        if grid[si+i][sj+j] == 'B':
                            nb += 1

                if nb in {0,1,3,4}:
                    return True
                    
        return False