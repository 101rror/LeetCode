/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function (s) {
    let stack = [];

    for (let c of s) {
        if (!isNaN(c) && stack.length) {
            stack.pop();
        }
        else {
            stack.push(c);
        }
    }

    return stack.join("");
};