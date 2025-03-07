class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> mp;

        for (int i = 0; i <= n - k; ++i) {
            unordered_set<int> st(nums.begin() + i, nums.begin() + i + k);
            for (int num : st) {
                mp[num]++;
            }
        }

        int ans = -1;
        for (const auto& [num, count] : mp) {
            if (count == 1 && num > ans) {
                ans = num;
            }
        }

        return ans;
    }
};