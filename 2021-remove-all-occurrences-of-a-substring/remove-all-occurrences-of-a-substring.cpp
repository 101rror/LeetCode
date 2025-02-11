class Solution {
public:
    string removeOccurrences(string s, string part) {
        int plen = part.length();

        while (s.find(part) != string::npos) {
            int idx = s.find(part);

            s = s.substr(0, idx) + s.substr(idx + plen);
        }

        return s;
    }
};