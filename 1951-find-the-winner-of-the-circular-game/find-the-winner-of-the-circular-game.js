/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function (n, k) {
    let ans = 0;

    for (let i = 2; i < n + 1; i++) {
        ans = (ans + k) % i;
    }

    return ans + 1;
};