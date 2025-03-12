/**
 * @param {number[]} nums
 * @return {number}
 */
let maximumCount = function (nums) {
    let p = 0, n = 0;

    for (num of nums) {
        if (num > 0) {
            p++;
        }
        else if (num < 0) {
            n++;
        }
    }

    return Math.max(p, n);
};