public class Solution {
    public long MaxTotalValue(int[] nums, int k) {
        int mn = nums[0], mx = nums[0];

        foreach (int num in nums) {
            mn = Math.Min(mn, num);
            mx = Math.Max(mx, num);
        }

        return (long) (mx - mn) * k;
    }
}