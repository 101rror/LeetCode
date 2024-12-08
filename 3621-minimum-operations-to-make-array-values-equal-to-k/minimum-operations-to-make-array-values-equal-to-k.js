/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function (nums, k) {
    const seen = new Set(nums);
    let count = 0;

    for (const num of seen) {
        if (num < k) {
            return -1;
        }
        else if (num > k) {
            count += 1;
        }
    }

    return count;
};