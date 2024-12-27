/**
 * @param {number[]} values
 * @return {number}
 */
var maxScoreSightseeingPair = function (values) {
    const n = values.length;
    let mx = 0, cur = 0;

    for (let i = 1; i < n; i++) {
        cur = Math.max(cur, values[i - 1] + i - 1);
        mx = Math.max(mx, cur + values[i] - i);
    }

    return mx;
};