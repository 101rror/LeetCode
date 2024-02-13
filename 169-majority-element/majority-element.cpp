class Solution {
public:
    int majorityElement(vector<int>& nums)
    {
        int n = nums.size();
        int x = (n / 2);
        unordered_map<int, int>mp;

        for(auto &it: nums)
        {
            mp[it]++;
        }

        for(auto &it: mp)
        {
            if(it.second > x)
            {
                return it.first;
            }
        }

        return 0;
    }
};