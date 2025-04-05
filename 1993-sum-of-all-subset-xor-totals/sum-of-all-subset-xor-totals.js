/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function (nums) {
    let ans = 0;

    for (let num of nums) {
        ans |= num;
    }

    return ans << (nums.length - 1);
};