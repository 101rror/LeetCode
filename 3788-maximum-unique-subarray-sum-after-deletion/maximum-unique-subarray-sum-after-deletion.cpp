class Solution {
public:
    int maxSum(vector<int>& nums) {
        set<int> st;
        int maxsum = 0;

        for (auto num : nums) {
            if (num > 0 && st.find(num) == st.end()) {
                maxsum += num;
            }
            st.insert(num);
        }

        return maxsum > 0 ? maxsum : *max_element(nums.begin(), nums.end());
    }
};