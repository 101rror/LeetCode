/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function (words, queries) {
    const n = words.length;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);

    const dp = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        if (vowels.has(words[i][0]) && vowels.has(words[i][words[i].length - 1])) {
            dp[i] = 1;
        }
    }

    const prefixSum = Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + dp[i];
    }

    const result = [];
    for (const [start, end] of queries) {
        result.push(prefixSum[end + 1] - prefixSum[start]);
    }

    return result;
};