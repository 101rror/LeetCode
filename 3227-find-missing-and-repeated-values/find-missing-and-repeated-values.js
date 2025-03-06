/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function (grid) {
    let n = grid.length;
    let size = n * n;
    let count = new Array(size + 1).fill(0);

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            count[grid[i][j]]++;
        }
    }

    let a = -1, b = -1;

    for (let num = 1; num <= size; num++) {
        if (count[num] === 2) {
            a = num;
        } else if (count[num] === 0) {
            b = num;
        }
    }

    return [a, b];
};