public class Solution {
    public int[][] RangeAddQueries(int n, int[][] queries) {
        var mat = new int[n][];

        for (int i = 0; i < n; i++) {
            mat[i] = new int[n];
        }

        for (int i = 0; i < queries.Length; i++) {
            int row1 = queries[i][0], row2 = queries[i][2];
            int col1 = queries[i][1], col2 = queries[i][3];

            for (int j = row1; j <= row2; j++) {
                mat[j][col1]++;
                if (col2 + 1 < n) {
                    mat[j][col2 + 1]--;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j++) {
                mat[i][j] += mat[i][j - 1];
            }
        }

        return mat;
    }
}