class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string sub = "";

        for (string str : words) {
            for (char ch : str) {
                sub += ch;
            }
            if (sub == s) {
                return true;
            }
        }

        return false;
    }
};