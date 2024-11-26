/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findChampion = function (n, edges) {
    let dp = new Array(n).fill(0);
    let count = 0, champion = -1;

    for (const edge of edges) {
        dp[edge[1]] += 1;
    }

    for (let i = 0; i < n; i++) {
        if (dp[i] === 0) {
            count += 1;
            champion = i;
        }
    }

    return count === 1 ? champion : -1;
};