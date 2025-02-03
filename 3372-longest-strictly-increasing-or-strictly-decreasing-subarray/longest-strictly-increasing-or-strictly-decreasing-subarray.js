/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function (nums) {
    const n = nums.length;
    let inc = 1, dec = 1, ans = 1;

    for (let i = 1; i < n; i++) {
        if (nums[i - 1] < nums[i]) {
            dec = 1;
            inc += 1;
        }
        else if (nums[i - 1] > nums[i]) {
            inc = 1;
            dec += 1;
        }
        else {
            inc = 1;
            dec = 1;
        }

        ans = Math.max(ans, inc, dec);
    }

    return ans;
};