class Solution {
public:
    std::vector<int> transformArray(std::vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 0) {
                nums[i] = 0;
            } else {
                nums[i] = 1;
            }
        }
        
        std::sort(nums.begin(), nums.end());
        return nums;
    }
};