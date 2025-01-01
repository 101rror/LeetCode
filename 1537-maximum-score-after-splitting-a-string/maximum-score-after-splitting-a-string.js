/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function (s) {
    const n = s.length;
    let maxScore = 0;

    for (let i = 1; i < n; i++) {
        let left = s.substring(0, i);
        let right = s.substring(i, n);

        if (left.split("0").length - 1 > 0 || right.split("1").length - 1 > 0) {
            let zero = left.split("0").length - 1;
            let one = right.split("1").length - 1;

            maxScore = Math.max(maxScore, zero + one);
        }
    }

    return maxScore;
};