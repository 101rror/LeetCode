class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        unordered_set<int> seen(nums.begin(), nums.end());
        int count = 0;

        for (auto num : seen) {
            if (num < k) {
                return -1;
            }
            if (num > k) {
                count++;
            }
        }

        return count;
    }
};