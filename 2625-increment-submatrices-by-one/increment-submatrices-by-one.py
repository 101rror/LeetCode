import numpy as npy

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        temp = [[0] * n for _ in range(n)]
        mat = npy.array(temp)

        for x in queries:
            row1, row2 = x[0], x[2]
            coloumn1, coloumn2 = x[1], x[3]

            mat[row1 : row2 + 1, coloumn1 : coloumn2 + 1] += 1

        return mat.tolist()
