public class Solution {
    public int Search(int[] nums, int target) {
        int n = nums.Length;

        for (int i = 0; i < n; i++) {
            if (nums[i] == target) {
                return i;
            }
        }

        return -1;
    }
}