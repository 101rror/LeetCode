public class Solution {
    public int CountPermutations(int[] complexity) {
        int n = complexity.Length;

        for (int i = 1; i < n; i++) {
            if (complexity[i] <= complexity[0]) {
                return 0;
            }
        }

        long ans = 1;
        int mod = 1000000007;
        for (int i = 1; i < n; i++) {
            ans = (ans * i) % mod;
        }
        
        return (int)ans;
    }
}