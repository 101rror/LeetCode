/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid = function (s, locked) {
    const n = s.length;
    if (n % 2 != 0) {
        return false;
    }

    let count = 0;
    for (let i = 0; i < n; i++) {
        if (locked[i] === '0' || s[i] === '(') {
            count++;
        }
        else {
            count--;
        }
        if (count < 0) {
            return false;
        }
    }
    count = 0

    for (let i = n - 1; i >= 0; i--) {
        if (locked[i] === '0' || s[i] === ')') {
            count++;
        }
        else {
            count--;
        }
        if (count < 0) {
            return false;
        }
    }


    return true;
};