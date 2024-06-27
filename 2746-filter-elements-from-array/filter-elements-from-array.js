/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    const filterarray = [];

    for (var i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            filterarray.push(arr[i]);
        }
    }

    return filterarray;

};