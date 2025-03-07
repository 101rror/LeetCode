/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestInteger = function (nums, k) {
    let n = nums.length;
    let mp = new Map();

    for (let i = 0; i <= n - k; i++) {
        let unique = new Set(nums.slice(i, i + k));
        for (let num of unique) {
            mp.set(num, (mp.get(num) || 0) + 1);
        }
    }

    let ans = -1;
    for (let [num, count] of mp) {
        if (count === 1 && num > ans) {
            ans = num;
        }
    }

    return ans;
};