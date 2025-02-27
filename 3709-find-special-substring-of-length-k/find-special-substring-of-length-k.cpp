class Solution {
public:
    bool hasSpecialSubstring(string s, int k) {
        int n = s.size();
        int first = 0, last = 0;

        while (first < n) {
            if (s[first] != s[last]) {
                if (first - last == k) {
                    return true;
                }
                last = first;
            }
            first += 1;
        }

        return n - last == k;
    }
};