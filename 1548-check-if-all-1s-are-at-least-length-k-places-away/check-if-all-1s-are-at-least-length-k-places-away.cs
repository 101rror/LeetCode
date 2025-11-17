public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int n = nums.Length;
        int prev = -1;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                if (prev != -1 && i - prev - 1 < k) {
                    return false;
                }
                prev = i;
            }
        }

        return true;
    }
}