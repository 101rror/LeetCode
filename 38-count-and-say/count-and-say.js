/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function (n) {
    if (n === 1) {
        return "1";
    }

    return rle(countAndSay(n - 1));
};

function rle(s) {
    const n = s.length;
    let ans = "";
    let count = 1;

    for (let i = 1; i < n; i++) {
        if (s[i] === s[i - 1]) {
            count++;
        } else {
            ans += count + s[i - 1];
            count = 1;
        }
    }

    ans += count + s[s.length - 1];

    return ans;
}