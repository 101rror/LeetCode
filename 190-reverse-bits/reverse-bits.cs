public class Solution {
    public int ReverseBits(int n) {
        int ans = 0;

        for (int i = 0; i < 32; i++) {
            ans = ans << 1;
            ans += (n & 1);
            n = n >> 1;
        }
        
        return ans;
    }
}