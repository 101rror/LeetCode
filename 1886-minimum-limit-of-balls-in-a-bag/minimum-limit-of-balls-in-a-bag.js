/**
 * @param {number[]} nums
 * @param {number} maxOperations
 * @return {number}
 */
var minimumSize = function (nums, maxOperations) {
    let low = 1, high = Math.max(...nums);

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        let count = 0;

        if (nums.reduce((acc, num) => acc + Math.floor((num - 1) / mid), 0) <= maxOperations) {
            high = mid;
        }
        else {
            low = mid + 1;
        }
    }

    return high;
};