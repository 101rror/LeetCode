class Solution {
public:
    long long Power(long long base, long long exp, long long mod) {
        long long ans = 1;
        base %= mod;

        while (exp > 0) {
            if (exp % 2 == 1) {
                ans = (ans * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }

        return ans;
    }

    int countGoodNumbers(long long n) {
        long long even = 0, odd = 0;
        long long mod = 1e9 + 7;

        if (n % 2 == 0) {
            even = n / 2;
            odd = n / 2;
        } else {
            even = n / 2 + 1;
            odd = n / 2;
        }

        long long ans = (Power(5, even, mod) * Power(4, odd, mod)) % mod;

        return ans;
    }
};