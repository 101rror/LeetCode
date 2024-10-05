class Solution {
public:
    bool checkInclusion(string s1, string s2)
    {
        int len1 = s1.size();
        int len2 = s2.size();

        vector<int> count1(26, 0);

        for(auto x: s1)
        {
            count1[x - 'a']++;
        }

        for(int i = 0; i < (len2 - len1 + 1); i++)
        {
            vector<int> count2(26, 0);
            
            for(int j = i; j < (len1 + i); j++)
            {
                count2[s2[j] - 'a']++;
            }
            if(count1 == count2)
            {
                return true;
            }
        }
        return false;
    }
};