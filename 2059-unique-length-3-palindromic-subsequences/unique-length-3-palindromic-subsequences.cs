public class Solution {
    public int CountPalindromicSubsequence(string s) {
        string alpha = "abcdefghijklmnopqrstuvwxyz";
        int count = 0, left, right;
        HashSet<char> hash = new HashSet<char>();

        foreach (char c in alpha) {
            left = s.IndexOf(c);
            right = s.LastIndexOf(c);

            if (left != -1 && right != -1 && left < right) {
                for (int i = left + 1; i < right; i++) {
                    if (!hash.Contains(s[i])) {
                        count++;
                        hash.Add(s[i]);
                    }
                    if (hash.Count == 26) {
                        break;
                    }
                }
            }

            hash.Clear();
        }

        return count;
    }
}
