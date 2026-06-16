public class Solution {
    public string ProcessStr(string s) {
        StringBuilder ans = new StringBuilder();

        foreach (char ch in s) {
            if (ch == '*') {
                if (ans.Length > 0) {
                    ans.Remove(ans.Length - 1, 1);
                }
            }
            else if (ch == '#') {
                ans.Append(ans.ToString());
            }
            else if (ch == '%') {
                var arr = ans.ToString().ToCharArray();
                Array.Reverse(arr);
                ans.Clear();
                ans.Append(arr);
            }
            else {
                ans.Append(ch);
            }
        }

        return ans.ToString();
    }
}