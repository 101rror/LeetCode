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
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(all(nums));
        ll cur = LLONG_MIN, count = 0;

        for (auto it : nums) {
            ll left = it - k;
            ll right = it + k;
            if (cur < left) {
                cur = left;
            }
            if (cur <= right) {
                count++;
                cur++;
            }
        }

        return count;
    }
};