/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function (mat) {
    let n = mat.length;
    let tsum = 0, neg = 0, mn = Infinity;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] < 0) {
                neg++;
            }

            tsum += Math.abs(mat[i][j]);
            mn = Math.min(mn, Math.abs(mat[i][j]));
        }
    }

    if (neg % 2 != 0) {
        return tsum -= 2 * mn;
    }

    return tsum;
};