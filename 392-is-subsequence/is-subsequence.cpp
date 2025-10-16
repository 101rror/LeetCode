#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define mpi map<int, int>
#define mps map<string, int>
#define pb push_back
#define all(x) (x).begin(), (x).end()

const int MOD = 1e9 + 7;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n = s.length(), m = t.length();
        int x = 0;

        for (int i = 0; i < m and x < n; i++) {
            if (s[x] == t[i]) {
                x++;
            }
        }

        return (x == n);
    }
};