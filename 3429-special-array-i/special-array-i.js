/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isArraySpecial = function (nums) {
    let n = nums.length;

    for (let i = 1; i < n; i++) {
        if (nums[i - 1] % 2 === nums[i] % 2) {
            return false;
        }
    }
    return true;
};