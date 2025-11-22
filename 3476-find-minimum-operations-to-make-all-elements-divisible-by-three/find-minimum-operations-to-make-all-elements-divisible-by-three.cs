public class Solution {
    public int MinimumOperations(int[] nums) {
        int count = 0;

        foreach (int num in nums) {
            if (num % 3 != 0) {
                count++;
            }
        }

        return count;
    }
}