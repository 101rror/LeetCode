/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function (nums) {
    const seen = new Array(128).fill(false);
    const n = nums.length;

    for (let i = n - 1; i >= 0; i--) {
        if (seen[nums[i]]) {
            return Math.floor(i / 3) + 1;
        }

        seen[nums[i]] = true;
    }

    return 0;
};