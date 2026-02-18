public class Solution {
    public bool HasAlternatingBits(int n) {
        n = n ^ (n >> 1);
        
        return (n & (n + 1)) == 0;
    }
}