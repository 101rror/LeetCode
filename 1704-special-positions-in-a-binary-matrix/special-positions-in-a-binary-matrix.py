class Solution:    
    def numSpecial(self, mat: List[List[int]]) -> int:
        def column(matrix, i):
            return [row[i] for row in matrix]

        count = 0
        n = len(mat)

        for i in range(n):
            if(mat[i].count(1) == 1):
                i = mat[i].index(1)
                col = column(mat, i)
                if(col.count(1) == 1):
                    count += 1
        
        return count  
                
        
                