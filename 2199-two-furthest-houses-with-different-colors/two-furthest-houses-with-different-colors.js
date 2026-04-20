/**
 * @param {number[]} colors
 * @return {number}
 */
const maxDistance = A => {
    const n = A.length;
    let left = 0, right = 0;

    for (let i = 0; i < n; i++)
        if (A[i] ^ A.at(-1)) {
            left = i;
            break;
        }

    for (let i = n - 1; i >= 0; i--)
        if (A[i] ^ A[0]) {
            right = i;
            break;
        }

    return Math.max(n - 1 - left, right);
};