public class Solution {
    public long MaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        long[] dp = new long[k];
        long sum = 0, ans = long.MinValue;

        for(int i = 0; i < n; i++) {
            sum += nums[i];
            
            if (i + 1 >= k) {
                ans = Math.Max(ans, sum - dp[(i + 1) % k]);
                dp[(i + 1) % k] = Math.Min(dp[(i + 1) % k], sum);
            } else {
                dp[(i + 1) % k] = sum; 
            }
        }

        return ans;
    }
}