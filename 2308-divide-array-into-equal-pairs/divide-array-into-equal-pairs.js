/**
 * @param {number[]} nums
 * @return {boolean}
 */
var divideArray = function (nums) {
    let counter = new Map();

    for (let num of nums) {
        counter.set(num, (counter.get(num) || 0) + 1);
    }

    for (let count of counter.values()) {
        if (count % 2 !== 0) {
            return false;
        }
    }

    return true;
};