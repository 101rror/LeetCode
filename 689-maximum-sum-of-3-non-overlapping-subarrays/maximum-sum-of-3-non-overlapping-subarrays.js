/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays = function (nums, k) {
    const n = nums.length;
    const window = [nums.slice(0, k).reduce((a, b) => a + b, 0)];

    for (let i = 1; i < n - k + 1; i++) {
        x = nums.slice(i, i + k).reduce((a, b) => a + b, 0);
        window.push(x);
    }

    const wlen = window.length;
    const left = Array(wlen).fill(0);
    const right = Array(wlen).fill(0);

    let bestleft = 0;
    for (let i = 0; i < wlen; i++) {
        if (window[i] > window[bestleft]) {
            bestleft = i;
        }
        left[i] = bestleft;
    }

    let bestright = wlen - 1;
    for (let i = wlen - 1; i >= 0; i--) {
        if (window[i] >= window[bestright]) {
            bestright = i;
        }
        right[i] = bestright;
    }

    let maxsum = 0;
    let ans = Array(3).fill(-1);

    for (let i = k; i < wlen - k; i++) {
        let l = left[i - k], r = right[i + k];
        let threesum = window[l] + window[i] + window[r];

        if (threesum > maxsum) {
            maxsum = threesum;
            ans = [l, i, r];
        }
    }

    return ans;
};