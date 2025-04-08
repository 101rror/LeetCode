class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> seen;
        int count = 1, n = nums.size();

        seen.insert(nums.begin(), nums.end());

        if (seen.size() == n) {
            return 0;
        }

        for (int i = 3; i < n; i += 3) {
            seen.clear();
            bool isDistinct = true;

            for (int j = i; j < n; ++j) {
                if (seen.count(nums[j])) {
                    isDistinct = false;
                    break;
                }
                seen.insert(nums[j]);
            }
            if (isDistinct) {
                return count;
            }
            count++;
        }

        return count;
    }
};