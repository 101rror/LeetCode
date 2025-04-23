/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function (n) {
    const counter = new Map();

    for (let i = 1; i <= n; i++) {
        const key = i.toString().split('').reduce((sum, digit) => sum + Number(digit), 0);
        counter.set(key, (counter.get(key) || 0) + 1);
    }

    let maxCount = Math.max(...counter.values());
    let count = 0;

    for (let val of counter.values()) {
        if (val === maxCount) {
            count++;
        }
    }

    return count;
};