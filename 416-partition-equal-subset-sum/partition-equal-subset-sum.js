/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
    let total = nums.reduce((a, b) => a + b, 0);
    if (total % 2 !== 0) {
        return false;
    }

    let target = total / 2;
    let dp = new Array(target + 1).fill(false);
    dp[0] = true;

    for (let num of nums) {
        for (let i = target; i >= num; i--) {
            dp[i] = dp[i] || dp[i - num];
        }
    }

    return dp[target];
};