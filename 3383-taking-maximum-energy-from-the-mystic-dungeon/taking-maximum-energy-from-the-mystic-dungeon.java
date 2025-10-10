class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int l = energy.length;
        int[] dp = new int[l];
        int ans = Integer.MIN_VALUE;

        for (int i = l - 1; i >= 0; i--) {
            if (i + k < l) {
                dp[i] = energy[i] + dp[i + k];
            } else {
                dp[i] = energy[i];
            }
            ans = Math.max(ans, dp[i]);
        }

        return ans;
    }
}
