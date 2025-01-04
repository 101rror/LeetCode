/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function (s) {
    let count = 0;

    for (let i = 0; i < 26; i++) {
        let left = s.indexOf(String.fromCharCode(i + 97));
        let right = s.lastIndexOf(String.fromCharCode(i + 97));

        if (left != -1 && right != -1) {
            let substring = s.slice(left + 1, right);
            let uniqueChars = new Set(substring);
            count += uniqueChars.size;
        }
    }

    return count;
};