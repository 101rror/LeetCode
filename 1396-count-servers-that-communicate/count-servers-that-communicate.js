/**
 * @param {number[][]} grid
 * @return {number}
 */
var countServers = function (grid) {
    const r = grid.length, c = grid[0].length;
    let row = new Array(r).fill(0), col = new Array(c).fill(0);
    let count = 0

    for (let i = 0; i < r; i++) {
        for (let j = 0; j < c; j++) {
            if (grid[i][j] == 1) {
                row[i]++;
                col[j]++;
            }
        }
    }

    for (let i = 0; i < r; i++) {
        for (let j = 0; j < c; j++) {
            if (grid[i][j] == 1) {
                if (row[i] > 1 || col[j] > 1) {
                    count++;
                }
            }
        }
    }

    return count;
};