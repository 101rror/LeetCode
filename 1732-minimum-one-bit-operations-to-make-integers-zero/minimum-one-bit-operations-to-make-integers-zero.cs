public class Solution {
    public int MinimumOneBitOperations(int n) {
        int count = 0;

        while (n > 0) {
            count ^= n;
            n >>= 1;
        }

        return count;
    }
}