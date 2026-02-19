public class Solution {
    public int CountBinarySubstrings(string s) {
        int n = s.Length;
        int count = 0, prev = 0, curr = 1;
        
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1]) {
                curr++;
            }
            else {
                count += Math.Min(prev, curr);
                prev = curr;
                curr = 1;
            }
        }
        
        count += Math.Min(prev, curr);
        return count;
    }
}