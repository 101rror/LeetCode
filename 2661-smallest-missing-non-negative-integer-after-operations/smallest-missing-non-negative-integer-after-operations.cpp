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
    int findSmallestInteger(vector<int>& nums, int value) {
        int n = nums.size();
        int ans = 0;
        mpi mp;

        for (auto it : nums) {
            int rem = it % value;

            while (rem < 0) {
                rem += value;
            }
            mp[rem]++;
        }

        for (int i = 0; i <= n; i++) {
            int rem = i % value;

            if (mp[rem] <= 0) {
                ans = i;
                break;
            } else {
                mp[rem]--;
            }
        }

        return ans;
    }
};