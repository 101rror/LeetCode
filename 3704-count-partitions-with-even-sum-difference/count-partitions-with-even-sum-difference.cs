public class Solution {
    public int CountPartitions(int[] nums) {
        int n = nums.Length, tSum = 0;
    
        foreach (int num in nums) {
            tSum += num;
        }
    
        int left = 0, count = 0;
    
        for (int i = 0; i < n - 1; i++) {
            left += nums[i];
            int right = tSum - left;
        
            if (((left - right) & 1) == 0) {
                count++;
            }
        }
        
        return count;
    }
}