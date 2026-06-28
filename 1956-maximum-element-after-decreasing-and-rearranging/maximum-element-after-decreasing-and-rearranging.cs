public class Solution {
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr) {
        int n = arr.Length;
        Array.Sort(arr);
        int ans = 1;

        for (int i = 1; i < n; i++) {
            if (arr[i] >= ans + 1) {
                ans++;
            }
        }

        return ans;
    }
}