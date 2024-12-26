/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function (n, x) {
    const dp = Array(n + 1).fill(0);
    const mod = 10 ** 9 + 7;

    dp[0] = 1;

    for (let i = 1; i < n + 1; i++) {
        let m = i ** x;
        if (m > n) {
            break;
        }
        for (let j = n; j >= m; j--) {
            dp[j] += dp[j - m];
        }
    }

    return dp[n] % mod;
};