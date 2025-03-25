/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
    let ans = "";
    let n1 = word1.length, n2 = word2.length;

    for (let i = 0; i < Math.max(n1, n2); i++) {
        if (n1 > i) {
            ans += word1[i];
        }
        if (n2 > i) {
            ans += word2[i];
        }
    }

    return ans;
};