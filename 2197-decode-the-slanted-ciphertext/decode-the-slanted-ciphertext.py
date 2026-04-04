class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        idx = 0

        mat, ans = [], []

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(encodedText[idx])
                idx += 1
            mat.append(row)

        for start in range(cols):
            i, j = 0, start
            while i < rows and j < cols:
                ans.append(mat[i][j])
                i += 1
                j += 1

        return "".join(ans).rstrip()
