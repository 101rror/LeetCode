public class Solution {
    public int MinElement(int[] nums) {
        int ans = int.MaxValue;

        foreach (int num in nums) {
            int x = num, sum = 0;

            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }

            ans = Math.Min(ans, sum);
        }

        return ans;
    }
}