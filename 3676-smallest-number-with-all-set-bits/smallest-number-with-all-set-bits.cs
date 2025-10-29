public class Solution {
    public int SmallestNumber(int n) {
        int x = 1;

        while(x < n) {
            x = x * 2 + 1;
        }

        return x;
    }
}