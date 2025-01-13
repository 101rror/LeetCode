/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function (s) {
    const n = s.length;
    let freq = {};

    for (const ch of s) {
        freq[ch] = (freq[ch] || 0) + 1;
    }

    let removeCount = 0

    for (const [key, val] of Object.entries(freq)) {
        if (val > 2 && val % 2 != 0) {
            removeCount += (val - 1);
        }
        else if (val > 2 && val % 2 === 0) {
            removeCount += (val - 2);
        }
    }

    return n - removeCount;
};