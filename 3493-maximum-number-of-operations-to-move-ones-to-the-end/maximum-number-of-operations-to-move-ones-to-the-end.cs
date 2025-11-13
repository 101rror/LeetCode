public class Solution {
    public int MaxOperations(string s) {
        int n = s.Length;
        int one = 0, ans = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                one++;
            }
            else if (i > 0 && s[i - 1] == '1') {
                ans += one;
            }
        }

        return ans;
    }
}