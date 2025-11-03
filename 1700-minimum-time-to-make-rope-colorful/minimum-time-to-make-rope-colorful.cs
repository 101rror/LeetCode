public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int n = colors.Length;
        int ans = 0, mx = neededTime[0];

        for (int i = 1; i < n; i++) {
            if (colors[i - 1] == colors[i]) {
                ans += Math.Min(mx, neededTime[i]);
                mx = Math.Max(mx, neededTime[i]);
            }
            else {
                mx = neededTime[i];
            }
        }

        return ans;
    }
}