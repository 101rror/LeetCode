class Solution {
public:
    int numberOfSubstrings(string s) {
        vector<int> idx(3, 0);
        int count = 0;

        for (int i = 0; i < s.length(); ++i) {
            idx[s[i] - 'a'] = i + 1;

            count += *min_element(idx.begin(), idx.end());
        }

        return count;
    }
};