public class Solution {
    public int MinNumberOperations(int[] target) {
        int prev = 0, ans = 0;

        foreach(int num in target) {
            if(num > prev) {
                ans += (num - prev);
            }

            prev = num;
        }

        return ans;
    }
}