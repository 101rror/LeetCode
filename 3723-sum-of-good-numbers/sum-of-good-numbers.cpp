class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int n = nums.size();
        int goodSum = 0;

        for (int i = 0; i < n; ++i) {
            if (i - k >= 0 && nums[i] <= nums[i - k]) {
                continue;
            }
            if (i + k < n && nums[i] <= nums[i + k]) {
                continue;
            }
            goodSum += nums[i];
        }

        return goodSum;
    }
};