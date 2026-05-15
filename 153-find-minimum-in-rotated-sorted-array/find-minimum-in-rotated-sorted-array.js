/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (arr) {
    let first = 0, last = arr.length - 1;

    while (first < last) {
        let mid = Math.floor((first + last) / 2);

        if (arr[mid] > arr[last]) {
            first = mid + 1;
        }
        else {
            last = mid;
        }
    }

    return arr[first];
};