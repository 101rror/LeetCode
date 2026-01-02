class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_set<int> seen;

        for (int it : nums) {
            if (seen.count(it)) {
                return it;
            }
            seen.insert(it);
        }
        return -1;
    }
};