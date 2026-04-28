/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function (grid, x) {
    let nums = [];

    for (let row of grid) {
        for (let val of row) {
            nums.push(val);
        }
    }

    let rem = nums[0] % x;

    for (let num of nums) {
        if (num % x !== rem) {
            return -1;
        }
    }

    nums.sort((a, b) => a - b);

    let median = nums[Math.floor(nums.length / 2)];

    let ops = 0;

    for (let num of nums) {
        ops += Math.abs(num - median) / x;
    }

    return ops;
};