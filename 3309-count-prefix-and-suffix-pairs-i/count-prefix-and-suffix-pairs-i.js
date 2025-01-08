/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function (words) {
    function isPrefixAndSuffix(x, s) {
        return s.startsWith(x) && s.split('').reverse().join('').startsWith(x.split('').reverse().join(''));
    }

    const n = words.length;
    let count = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (words[i].length <= words[j].length) {
                if (isPrefixAndSuffix(words[i], words[j])) {
                    count += 1;
                }
            }
        }
    }

    return count;
};