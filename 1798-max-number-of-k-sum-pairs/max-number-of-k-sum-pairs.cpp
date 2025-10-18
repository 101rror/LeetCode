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
    int maxOperations(vector<int>& nums, int k) {
        umpi freq;
        ll ans = 0;

        for (auto num : nums) {
            ll comp = k - num;

            if (freq[comp] > 0) {
                ans++;
                freq[comp]--;
            } else {
                freq[num]++;
            }
        }

        return ans;
    }
};