class Solution {
public:
    int maxDifference(string s) {
        vector<int> freq(26, 0);

        for (char c : s) {
            freq[c - 'a']++;
        }

        int mx = INT_MIN;
        int mn = INT_MAX;

        for (int count : freq) {
            if (count > 0) {
                if (count % 2 == 0) {
                    mn = min(mn, count);
                } else {
                    mx = max(mx, count);
                }
            }
        }

        return mx - mn;
    }
};