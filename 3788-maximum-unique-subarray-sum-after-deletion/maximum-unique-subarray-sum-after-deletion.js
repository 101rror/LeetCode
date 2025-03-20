/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function (nums) {
    let set = new Set();
    let maxsum = 0;

    for (let num of nums) {
        if (num > 0 && !set.has(num)) {
            maxsum += num;
        }
        set.add(num);
    }

    return maxsum > 0 ? maxsum : Math.max(...nums);
};