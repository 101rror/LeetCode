/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function (target, arr) {
    let sortedarr = arr.sort((a, b) => a - b);
    let sortedtarget = target.sort((a, b) => a - b);

    if (sortedtarget.length !== sortedarr.length) {
        return false;
    }

    for (let i = 0; i < arr.length; i++) {
        if (sortedarr[i] !== sortedtarget[i]) {
            return false;
        }
    }

    return true;
};