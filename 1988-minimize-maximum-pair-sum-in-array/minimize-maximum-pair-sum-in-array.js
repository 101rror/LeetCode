/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function (nums) {
    const n = nums.length;
    let maxsum = 0;
    nums.sort((a, b) => a - b);

    for (let i = 0; i < n / 2; i++) {
        maxsum = Math.max(maxsum, nums[i] + nums[n - i - 1]);
    }

    return maxsum;
};