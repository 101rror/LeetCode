/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function (boxes) {
    const n = boxes.length;
    let dp = new Array(n).fill(0);
    let leftCount = 0, rightCount = 0, leftCost = 0, rightCost = 0

    for (let i = 1; i < n; i++) {
        if (boxes[i - 1] === "1") {
            leftCount += 1;
        }
        leftCost += leftCount;
        dp[i] = leftCost;
    }

    for (let i = n - 2; i >= 0; i--) {
        if (boxes[i + 1] === "1") {
            rightCount += 1;
        }
        rightCost += rightCount;
        dp[i] += rightCost;
    }

    return dp;
};