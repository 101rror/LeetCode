/**
 * @param {string} str1
 * @param {string} str2
 * @return {boolean}
 */
var canMakeSubsequence = function (str1, str2) {
    let alpha = 'abcdefghijklmnopqrstuvwxyza';
    let i = 0, j = 0;
    let n = str1.length, m = str2.length;

    while (i < n && j < m) {
        if (str1[i] === str2[j]) {
            j++;
        }
        else if (String.fromCharCode((str1[i].charCodeAt(0) - 'a'.charCodeAt(0) + 1) % 26 + 'a'.charCodeAt(0)) === str2[j]) {
            j++;
        }
        i++;
    }

    return j == m;
};