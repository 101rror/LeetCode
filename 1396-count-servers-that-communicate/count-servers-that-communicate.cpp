class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int r = grid.size(), c = grid[0].size();
        vector<int> row(r, 0), col(c, 0);
        int count = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    row[i]++;
                    col[j]++;
                }
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    if (row[i] > 1 || col[j] > 1) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
};