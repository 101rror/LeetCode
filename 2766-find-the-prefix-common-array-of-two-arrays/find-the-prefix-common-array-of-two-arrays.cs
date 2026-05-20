public class Solution {
    public int[] FindThePrefixCommonArray(int[] A, int[] B) {
        int n = A.Length;
        int[] ans = new int[n];
        int[] freq = new int[n + 1];
        int common = 0;

        for (int i = 0; i < n; i++) {
            freq[A[i]]++;
            if (freq[A[i]] == 2) {
                common++;
            }

            freq[B[i]]++;
            if (freq[B[i]] == 2) {
                common++;
            }

            ans[i] = common;
        }

        return ans;
    }
}