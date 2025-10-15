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
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = 0;

        while (right < n) {
            if (nums[right] != 0) {
                swap(nums[right], nums[left]);
                left++;
            }
            right++;
        }
    }
};