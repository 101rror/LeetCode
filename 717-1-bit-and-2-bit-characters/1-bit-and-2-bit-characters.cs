public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int n = bits.Length;
        int i = 0;

        while (i < n - 1) {
            if (bits[i] == 1) {
                i += 2;
            } else {
                i += 1;
            }
        }

        return i == n - 1;
    }
}