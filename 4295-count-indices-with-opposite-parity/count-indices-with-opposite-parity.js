/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countOppositeParity = function (nums) {
    const n = nums.length;
    const ans = new Array(n).fill(0);

    let even = 0;

    for (let x of nums) {
        if (x % 2 === 0) {
            even++;
        }
    }

    let odd = n - even;

    for (let i = 0; i < n; i++) {
        if (nums[i] % 2 === 0) {
            even--;
            ans[i] = odd;
        } else {
            odd--;
            ans[i] = even;
        }
    }

    return ans;
};