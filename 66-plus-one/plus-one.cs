public class Solution {
    public int[] PlusOne(int[] digits) {
        int n = digits.Length;

        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }

            digits[i] = 0;
        }

        int[] ans = new int[n + 1];
        ans[0] = 1;

        return ans;
    }
}