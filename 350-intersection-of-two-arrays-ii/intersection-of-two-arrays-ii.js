/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
    nums1.sort((a, b) => a - b);
    nums2.sort((a, b) => a - b);
    len1 = nums1.length;
    len2 = nums2.length;
    const ans = [];
    let i = 0, j = 0;

    while (i < len1 && j < len2) {
        if (nums1[i] < nums2[j]) {
            i++;
        }
        else if (nums1[i] > nums2[j]) {
            j++;
        }
        else {
            ans.push(nums1[i]);
            i++;
            j++;
        }
    }

    return ans;
};