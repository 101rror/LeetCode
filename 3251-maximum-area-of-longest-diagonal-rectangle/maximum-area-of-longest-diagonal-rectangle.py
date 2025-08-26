class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        n = len(d)
        mx, m = 0, 0
        
        for i in range(n):
            x, y = d[i]
            
            t = x * x + y * y
            
            if (t > m) or (t == m and x * y > mx):
                mx = x * y
                m = t
                
        return mx