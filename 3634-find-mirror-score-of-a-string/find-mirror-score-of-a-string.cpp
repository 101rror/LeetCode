class Solution {
public:
    long long calculateScore(string s) {
        long long ans = 0;
        vector<stack<int>> stk(26);

        for (int i = 0; i < s.size(); ++i) {
            int v = s[i] - 'a';
            if (stk[25 - v].size()) {
                ans += i - stk[25 - v].top();
                stk[25 - v].pop();
            } else {
                stk[v].push(i);
            }
        }

        return ans;
    }
};