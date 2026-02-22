public class Solution {
    public int BinaryGap(int n) {
        int ans = 0, pos = 0, last = -1;

        while (n > 0) {
            if ((n & 1) == 1) {
                if (last != -1) {
                    ans = Math.Max(ans, pos - last);
                }
                last = pos;
            }
            n >>= 1;
            pos++;
        }

        return ans;
    }
}