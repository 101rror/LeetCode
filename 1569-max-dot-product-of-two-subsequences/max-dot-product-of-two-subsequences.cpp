class Solution {
public:
    int maxDotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        vector<int> dp(n + 1, INT_MIN), pre(n + 1, INT_MIN);

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                int curr = nums1[i - 1] * nums2[j - 1];
                dp[j] = max({curr, pre[j], dp[j - 1], curr + max(0, pre[j - 1])});
            }
            swap(dp, pre);
        }
        
        return pre[n];
    }
};