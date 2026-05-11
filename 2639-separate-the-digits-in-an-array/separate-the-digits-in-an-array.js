/**
 * @param {number[]} nums
 * @return {number[]}
 */
var separateDigits = function (nums) {
    let ans = [];

    for (let num of nums) {
        let str = num.toString();

        for (let ch of str) {
            ans.push(Number(ch));
        }
    }

    return ans;
};