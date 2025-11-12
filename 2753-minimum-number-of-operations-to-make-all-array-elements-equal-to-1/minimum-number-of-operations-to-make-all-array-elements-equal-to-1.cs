public class Solution {

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int MinOperations(int[] nums) {
        int n = nums.Length;

        int one = 0;
        foreach (int x in nums) {
            if (x == 1) {
                one++;
            }
        }

        if (one > 0) {
            return n - one;
        }

        int tGcd = 0;
        foreach (int x in nums) {
            tGcd = gcd(tGcd, x);
        }

        if (tGcd > 1)
            return -1;

        int check = n;
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = i; j < n; j++) {
                cur = gcd(cur, nums[j]);
                if (cur == 1) {
                    check = Math.Min(check, j - i + 1);
                    break;
                }
            }
        }

        return check + n - 2;
    }
}