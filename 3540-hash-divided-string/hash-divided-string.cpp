class Solution {
public:
    string stringHash(string s, int k) {
        string alpha = "abcdefghijklmnopqrstuvwxyz";
        string ans = "";
        int n = s.length();

        for (int i = 0; i < n; i += k) {
            int hsum = 0;
            string substring = s.substr(i, k);

            for (char ch : substring) {
                hsum += alpha.find(ch);
            }

            int x = hsum % 26;
            ans += alpha[x];
        }

        return ans;
    }
};