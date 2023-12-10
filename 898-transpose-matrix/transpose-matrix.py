class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        ans = []

        for _ in range(c):
            x = []
            for _ in range(r):
                x.append(0)
            ans.append(x)

        for i in range(0, c):
            for j in range(0, r):
                ans[i][j] = mat[j][i]

        return ans