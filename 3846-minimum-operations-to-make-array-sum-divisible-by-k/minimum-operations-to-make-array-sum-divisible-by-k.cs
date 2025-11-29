public class Solution {
    public int MinOperations(int[] nums, int k) {
        int sum = 0;

        foreach (int num in nums) {
            sum += num;
        }
        
        return sum % k;
    }
}