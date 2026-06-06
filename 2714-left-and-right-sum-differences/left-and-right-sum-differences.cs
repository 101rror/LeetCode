public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        int total = 0;

        foreach (int x in nums) {
            total += x;
        }

        int left = 0;
        int[] ans = new int[nums.Length];

        for (int i = 0; i < nums.Length; i++) {
            total -= nums[i];
            ans[i] = Math.Abs(left - total);
            left += nums[i];
        }

        return ans;
    }
}