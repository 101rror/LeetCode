/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function (nums) {
    const n = nums.length;
    let ans = [];

    for (let i = 0; i < n; i++) {
        ans.push(nums[nums[i]]);
    }

    return ans;
};