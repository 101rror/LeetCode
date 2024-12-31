/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function (days, costs) {
    const n = days.length;
    const last = days[n - 1];
    let dp = new Array(last + 1).fill(0);
    const setdays = new Set(days);

    for (let i = 1; i < last + 1; i++) {
        if (setdays.has(i)) {
            dp[i] = Math.min(
                costs[0] + dp[i - 1],
                costs[1] + dp[Math.max(i - 7, 0)],
                costs[2] + dp[Math.max(i - 30, 0)]);
        }
        else {
            dp[i] = dp[i - 1];
        }
    }

    return dp[last];
};