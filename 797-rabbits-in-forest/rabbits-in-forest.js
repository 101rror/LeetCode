/**
 * @param {number[]} answers
 * @return {number}
 */
const numRabbits = (a) => {
    const m = new Int16Array(1000).fill(0);

    for (const x of a) {
        ++m[x];
    }

    let count = 0;

    for (let i = 0; i < 1000; ) {
        const c = m[i++];
        if (c) {
            count += i * Math.ceil(c / i);
        }
    }
    return count;
};