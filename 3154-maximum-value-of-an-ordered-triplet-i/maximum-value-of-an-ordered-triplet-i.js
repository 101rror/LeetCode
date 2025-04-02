/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function (nums) {
    const n = nums.length;
    let ans = 0;
    const leftMax = new Array(n).fill(0);
    const rightMax = new Array(n).fill(0);

    for (let i = 1; i < n; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], nums[i - 1]);
        rightMax[n - 1 - i] = Math.max(rightMax[n - i], nums[n - i]);
    }

    for (let j = 1; j < n - 1; j++) {
        ans = Math.max(ans, (leftMax[j] - nums[j]) * rightMax[j]);
    }

    return ans;
};