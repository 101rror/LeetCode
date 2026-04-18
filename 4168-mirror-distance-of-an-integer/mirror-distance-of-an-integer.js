/**
 * @param {number} n
 * @return {number}
 */
var mirrorDistance = function (n) {
    let rev = 0;
    let temp = n;

    while (temp > 0) {
        let digit = temp % 10;
        rev = rev * 10 + digit;
        temp = Math.floor(temp / 10);
    }

    return Math.abs(n - rev);
};