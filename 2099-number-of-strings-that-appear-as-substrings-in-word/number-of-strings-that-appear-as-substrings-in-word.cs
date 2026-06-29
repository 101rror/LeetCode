public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        int count = 0;

        foreach (string pattern in patterns) {
            if (word.Contains(pattern)) {
                count++;
            }
        }

        return count;
    }
}