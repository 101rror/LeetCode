public class Solution {
    public int[] LimitOccurrences(int[] nums, int k) {
        int count = 0;

        foreach (int num in nums) {
            if (count < k || num != nums[count - k]) {
                nums[count] = num;
                count++;
            }
        }

        int[] ans = new int[count];

        for (int i = 0; i < count; i++) {
            ans[i] = nums[i];
        }

        return ans;
    }
}