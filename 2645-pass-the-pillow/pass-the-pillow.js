/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function (n, time) {
    let r = Math.floor(time % (n - 1));
    let q = Math.floor(time / (n - 1));

    if (q % 2 === 0) {
        return (r + 1);
    }
    else {
        return (n - r);
    }
};