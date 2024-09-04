/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var stringHash = function (s, k) {
    const alpha = 'abcdefghijklmnopqrstuvwxyz';
    let ans = '';
    const n = s.length;

    for (let i = 0; i < n; i += k) {
        let hsum = 0;
        const substring = s.slice(i, i + k);

        for (let char of substring) {
            hsum += alpha.indexOf(char);
        }

        const x = hsum % 26;
        ans += alpha[x];
    }

    return ans;
};