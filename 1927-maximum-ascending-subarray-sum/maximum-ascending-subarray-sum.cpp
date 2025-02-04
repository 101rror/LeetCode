class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int n = nums.size();
        int subsum = 0, maxsum = INT_MIN;

        for (int i = 1; i < n; i++) {
            if (nums[i - 1] < nums[i]) {
                subsum += nums[i - 1];
            } else {
                subsum += nums[i - 1];
                maxsum = max(maxsum, subsum);
                subsum = 0;
            }
        }
        subsum += nums[n - 1];
        maxsum = max(maxsum, subsum);

        return maxsum;
    }
};