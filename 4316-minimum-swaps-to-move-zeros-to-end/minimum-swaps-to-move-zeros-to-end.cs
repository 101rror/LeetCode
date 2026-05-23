public class Solution {
    public int MinimumSwaps(int[] nums) {
        int n = nums.Length;
        int zero = 0, swap = 0;

        foreach (int num in nums) {
            if (num == 0) {
                zero++;
            }
        }

        for (int i = 0; i < n - zero; i++) {
            if (nums[i] == 0) {
                swap++;
            }
        }

        return swap;
    }
}