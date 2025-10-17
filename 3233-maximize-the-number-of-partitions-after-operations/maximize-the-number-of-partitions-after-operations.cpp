#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define mpi map<int, int>
#define mpll map<ll, ll>
#define mps map<string, int>
#define umpi unordered_map<int, int>
#define umpll unordered_map<ll, ll>
#define pb push_back
#define all(x) (x).begin(), (x).end()

const int MOD = 1e9 + 7;

class Solution {
public:
    umpll dp;
    ll solve(ll i, ll mask, ll change, int k, string& s) {
        int n = s.size();
        if (i == n) {
            return 1;
        }

        ll cur = (i << 27) | (mask << 1) | (change);

        if (dp.find(cur) != dp.end()) {
            return dp[cur];
        }

        int val = s[i] - 'a';
        ll nw = mask | (1 << val);

        int count = __builtin_popcount(nw);

        ll ans = 0;
        ll maxi = 0;

        if (count > k) {
            ans = 1 + solve(i + 1, 1 << val, change, k, s);
            maxi = max(maxi, ans);
        } else {
            ans = solve(i + 1, nw, change, k, s);
            maxi = max(maxi, ans);
        }

        if (change) {
            return dp[cur] = maxi;
        }

        for (int j = 0; j < 26; j++) {
            ll nw = mask | (1 << j);
            ll count = __builtin_popcount(nw);

            if (count > k) {
                maxi = max(maxi, 1 + solve(i + 1, 1 << j, 1, k, s));
            } else {
                maxi = max(maxi, solve(i + 1, nw, 1, k, s));
            }
        }

        return dp[cur] = maxi;
    }
    
    int maxPartitionsAfterOperations(string s, int k) {
        return solve(0, 0, 0, k, s);
    }
};