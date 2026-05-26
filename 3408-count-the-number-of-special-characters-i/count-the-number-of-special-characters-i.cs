public class Solution {
    public int NumberOfSpecialChars(string word) {
        HashSet<char> lower = new HashSet<char>();
        HashSet<char> upper = new HashSet<char>();

        foreach (char ch in word) {
            if (char.IsLower(ch)) {
                lower.Add(ch);
            }
            else {
                upper.Add(char.ToLower(ch));
            }
        }

        lower.IntersectWith(upper);

        return lower.Count;
    }
}