public class Solution {
    public int NumberOfSpecialChars(string word) {
        int n = word.Length;
        Dictionary<char, int> lastLower = new Dictionary<char, int>();
        Dictionary<char, int> firstUpper = new Dictionary<char, int>();

        for (int i = 0; i < n; i++) {
            char ch = word[i];

            if (char.IsLower(ch)) {
                lastLower[ch] = i;
            }
            else {
                char lower = char.ToLower(ch);

                if (!firstUpper.ContainsKey(lower)) {
                    firstUpper[lower] = i;
                }
            }
        }

        int count = 0;

        foreach (var kv in lastLower) {
            char ch = kv.Key;

            if (firstUpper.ContainsKey(ch) && lastLower[ch] < firstUpper[ch]) {
                count++;
            }
        }

        return count;
    }
}