class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();
        int inc = 1, dec = 1, ans = 1;

        for (int i = 1; i < n; i++) {
            if (nums[i - 1] < nums[i]) {
                dec = 1;
                inc += 1;
            } else if (nums[i - 1] > nums[i]) {
                inc = 1;
                dec += 1;
            } else {
                inc = 1;
                dec = 1;
            }

            ans = std::max(ans, std::max(inc, dec));
        }

        return ans;
    }
};