/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplitArray = function (nums) {
    const n = nums.length;
    const prefixsum = new Array(n).fill(0);
    prefixsum[0] = nums[0];

    for (let i = 1; i < n; i++) {
        prefixsum[i] = prefixsum[i - 1] + nums[i]
    }

    let count = 0;

    for (let i = 0; i < n - 1; i++) {
        if (prefixsum[i] >= prefixsum[n - 1] - prefixsum[i]) {
            count++;
        }
    }

    return count;
};