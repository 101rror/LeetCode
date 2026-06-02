public class Solution {
    public int MinimumCost(int[] cost) {
        Array.Sort(cost);
        Array.Reverse(cost);
        
        int n = cost.Length;
        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            if (i % 3 != 2) {
                ans += cost[i];
            }
        }
        
        return ans;
    }
}