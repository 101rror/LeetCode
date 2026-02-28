public class Solution {
    public int ConcatenatedBinary(int n) {
        const int MOD = 1000000007;
        long ans = 0;
        var pow = 2;

        for (int i = 1; i <= n; i++) {
            if (pow == i) {
                pow *= 2;
            }
            ans = (ans * pow + i) % MOD;
        }

        return (int)ans;
    }
}