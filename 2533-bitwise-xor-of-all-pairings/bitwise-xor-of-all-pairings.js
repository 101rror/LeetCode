/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums = function (nums1, nums2) {
    const n = nums1.length, m = nums2.length;
    let xor1 = 0, xor2 = 0, ans = 0;

    for (let num1 of nums1) {
        xor1 ^= num1;
    }
    for (let num2 of nums2) {
        xor2 ^= num2;
    }

    if (n % 2 === 1) {
        ans ^= xor2;
    }
    if (m % 2 === 1) {
        ans ^= xor1;
    }

    return ans;
};