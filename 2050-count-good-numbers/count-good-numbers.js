/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function (n) {
    const mod = BigInt(1e9 + 7);

    function power(base, exp, mod) {
        let ans = 1n;
        base = BigInt(base) % mod;
        exp = BigInt(exp);

        while (exp > 0) {
            if (exp % 2n === 1n) {
                ans = (ans * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2n;
        }

        return ans;
    }

    let even = Math.floor((n + 1) / 2);
    let odd = Math.floor(n / 2);

    let count = (power(5, even, mod) * power(4, odd, mod)) % mod;

    return Number(count);
};