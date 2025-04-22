/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */

var findClosest = function (x, y, z) {
    if (Math.abs(z - x) < Math.abs(z - y)) {
        return 1;
    } else if (Math.abs(z - y) < Math.abs(z - x)) {
        return 2;
    } else {
        return 0;
    }
};