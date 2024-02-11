class Solution:
    def modifiedMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        for i in range(col):
            k = 0
            for j in range(row):
                k = max(k, mat[j][i])
                
            for j in range(row):
                if mat[j][i] == -1:
                    mat[j][i] = k

        return mat