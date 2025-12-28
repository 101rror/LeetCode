public class Solution {
    public int CountNegatives(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int count = 0;

        for (int i = 0; i < m; i++) {
            while (n > 0) {
                if (grid[i][n - 1] >= 0) {
                    break;
                }

                count += (m - i);
                n--;
            }
        }
        
        return count;
    }
}