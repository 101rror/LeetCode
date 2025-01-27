/**
 * @param {string} s
 * @param {string[]} words
 * @return {boolean}
 */
var isPrefixString = function (s, words) {
    let i = 0;

    for (const word of words) {
        if (!s.startsWith(word, i)) {
            return false;
        }
        i += word.length;
        if (i == s.length) {
            return true;
        }
    }
    return false;
};