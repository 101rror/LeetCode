/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    const n = nums.length;
    const tsum = (n * (n + 1)) / 2;
    let csum = 0;

    for (let i = 0; i < nums.length; i++) {
        csum = csum + nums[i];
    }

    return tsum - csum;
};