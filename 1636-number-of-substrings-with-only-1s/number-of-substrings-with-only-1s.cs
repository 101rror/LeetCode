public class Solution {
    public int NumSub(string s) {
        const int MOD = 1000000007;
        long ans = 0, count = 0;

        foreach (char c in s) {
            if (c == '1') {
                count++;
            } else {
                ans += (count * (count + 1) / 2) % MOD;
                count = 0;
            }
        }
        ans += (count * (count + 1) / 2) % MOD;

        return (int)ans;
    }
}