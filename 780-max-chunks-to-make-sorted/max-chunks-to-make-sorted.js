/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function (arr) {
    let count = 0, dif = 0;

    for (let i = 0; i < arr.length; i++) {
        dif = dif + (arr[i] - i);
        if (dif == 0) {
            count++;
        }
    }

    return count;
};