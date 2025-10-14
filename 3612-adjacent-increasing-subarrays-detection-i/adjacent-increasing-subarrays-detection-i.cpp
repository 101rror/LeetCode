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
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = k - 1;

        if (count == 0) {
            return true;
        }

        for (int i = k + 1; i < n; i++) {
            if (nums[i] > nums[i - 1] && nums[i - k] > nums[i - k - 1]) {
                count--;
            } else {
                count = k - 1;
            }

            if (count == 0) {
                return true;
            }
        }

        return false;
    }
};