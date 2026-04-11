/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDistance = function (nums) {
    const mp = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (!mp.has(nums[i])) {
            mp.set(nums[i], []);
        }
        mp.get(nums[i]).push(i);
    }

    let ans = Infinity;

    for (const idx of mp.values()) {
        if (idx.length < 3) continue;

        for (let i = 0; i + 2 < idx.length; i++) {
            const distance = 2 * (idx[i + 2] - idx[i]);
            ans = Math.min(ans, distance);
        }
    }

    return ans === Infinity ? -1 : ans;
};