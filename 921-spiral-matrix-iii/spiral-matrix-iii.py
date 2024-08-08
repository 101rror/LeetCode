class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = [[rStart, cStart]]
        steps = d = 0
        
        while len(ans) < rows * cols:
            if d % 2 == 0:
                steps += 1
            
            for _ in range(steps):
                rStart += dir[d][0]
                cStart += dir[d][1]
                
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                
                if len(ans) == rows * cols:
                    return ans

            d = (d + 1) % 4
        
        return ans