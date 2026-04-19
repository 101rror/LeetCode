/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDistance = function (nums1, nums2) {
    const n1 = nums1.length, n2 = nums2.length;
    let i = 0, res = 0;

    for (let j = 0; j < n2; j++) {
        while (i < n1 && nums1[i] > nums2[j]) {
            i++;
        }
        if (i === n1)
            break;

        res = Math.max(res, j - i);
    }

    return res;
};