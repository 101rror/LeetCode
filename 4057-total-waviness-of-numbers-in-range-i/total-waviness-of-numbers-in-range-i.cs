public class Solution {
    public int TotalWaviness(int num1, int num2) {
        int Waviness(int num) {
            string s = num.ToString();
            int n = s.Length;
            int count = 0;

            for (int i = 1; i < n - 1; i++) {
                if ((s[i - 1] < s[i] && s[i] > s[i + 1]) || (s[i - 1] > s[i] && s[i] < s[i + 1])) {
                    count++;
                }
            }

            return count;
        }

        int total = 0;

        for (int num = num1; num <= num2; num++) {
            total += Waviness(num);
        }

        return total;
    }
}