/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    let first = 0, last = nums.length - 1;

    while (first < last) {
        let mid = Math.floor(first + (last - first) / 2);

        if (nums[mid] > nums[last]) {
            first = mid + 1;
        }
        else if (nums[mid] < nums[last]) {
            last = mid;
        }
        else {
            last--;
        }
    }

    return nums[first];
};