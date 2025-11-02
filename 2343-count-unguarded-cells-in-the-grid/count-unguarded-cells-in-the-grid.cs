public class Solution {
    public int CountUnguarded(int m, int n, int[][] guards, int[][] walls) {
        HashSet<(int, int)> blockedCells = new HashSet<(int, int)>();
        HashSet<(int, int)> guardedCells = new HashSet<(int, int)>();

        foreach (var wall in walls) {
            blockedCells.Add((wall[0], wall[1]));
        }
        foreach (var guard in guards) {
            blockedCells.Add((guard[0], guard[1]));
        }

        int[] dx = { -1, 0, 1, 0 };
        int[] dy = { 0, 1, 0, -1 };

        foreach (var guard in guards) {
            int x = guard[0];
            int y = guard[1];

            for (int d = 0; d < 4; d++) {
                int nx = x;
                int ny = y;

                while (true) {
                    nx += dx[d];
                    ny += dy[d];

                    if (nx < 0 || ny < 0 || nx >= m || ny >= n || blockedCells.Contains((nx, ny))) {
                        break;
                    }

                    guardedCells.Add((nx, ny));
                }
            }
        }

        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                var cell = (i, j);
                if (!blockedCells.Contains(cell) && !guardedCells.Contains(cell)) {
                    count++;
                }
            }
        }

        return count;
    }
}