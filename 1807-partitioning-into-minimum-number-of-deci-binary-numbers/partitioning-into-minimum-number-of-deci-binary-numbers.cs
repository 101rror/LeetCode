public class Solution {
    public int MinPartitions(string n) {
        int mx = 0;

        foreach (char c in n) {
            mx = Math.Max(mx, c - '0');
        }

        return mx;
    }
}