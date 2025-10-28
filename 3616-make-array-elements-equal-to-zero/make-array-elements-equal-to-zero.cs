public class Solution {
    public int CountValidSelections(int[] nums) {
        int n = nums.Length, count = 0, left = 0, right = nums.Sum();

        for (int i = 0; i < n; i++) {
            left += nums[i];
            right -= nums[i];

            if (nums[i] != 0) {
                continue;
            }
            if (left == right) {
                count += 2;
            }
            if (Math.Abs(left - right) == 1) {
                count++;
            }
        }

        return count;
    }
}