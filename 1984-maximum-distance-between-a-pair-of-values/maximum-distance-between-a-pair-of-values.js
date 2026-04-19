/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDistance = function (nums1, nums2) {
    let distance = 0;
    let i = 0, j = 0;

    while (j < nums2.length && i < nums1.length) {
        if (nums1[i] <= nums2[j]) {
            distance = Math.max(distance, j - i);
            j++;
        }
        else if (i < j) {
            i++;
        }
        else {
            i++;
            j++;
        }
    }

    return distance;
};