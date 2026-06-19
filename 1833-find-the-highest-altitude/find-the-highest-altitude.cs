public class Solution {
    public int LargestAltitude(int[] gain) {
        int pre = 0, ans = 0;

        foreach (int g in gain) {
            pre += g;

            if (pre > ans) {
                ans = pre;
            }
        }

        return ans;
    }
}