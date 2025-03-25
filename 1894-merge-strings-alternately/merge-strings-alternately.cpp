class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        string ans = "";

        for (int i = 0; i < max(n1, n2); i++) {
            if (!word1.empty()) {
                ans += word1[0];
                word1.erase(0, 1);
            }
            if (!word2.empty()) {
                ans += word2[0];
                word2.erase(0, 1);
            }
        }

        return ans;
    }
};