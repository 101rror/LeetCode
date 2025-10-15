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
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        int up = 1, preUp = 0;
        int ans = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                up++;
            } else {
                preUp = up;
                up = 1;
            }

            int half = up >> 1;
            int m = min(preUp, up);
            int maxc = max(half, m);
            ans = max(ans, maxc);
        }

        return ans;
    }
};