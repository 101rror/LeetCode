class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int dp[82] = {0};
        int ans = -1;

        for (int x : nums) {
            int sum = 0, temp = x;

            while (temp != 0) {
                sum += temp % 10;
                temp /= 10;
            }

            if (dp[sum] != 0) {
                ans = std::max(ans, x + dp[sum]);
            }
            dp[sum] = std::max(dp[sum], x);
        }

        return ans;
    }
};