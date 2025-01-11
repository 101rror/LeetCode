/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var canConstruct = function (s, k) {
    const n = s.length;
    
    if (n < k) {
        return false;
    }

    let odd = 0;
    let mp = new Map();

    for (let ch of s) {
        mp.set(ch, (mp.get(ch) || 0) + 1);
    }

    for (let [key, val] of mp) {
        if (val % 2 != 0) {
            odd++;
        }
    }

    if (n == k || odd <= k) {
        return true;
    }
    return false;
};