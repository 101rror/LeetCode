class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k)
    {
        long long len = gifts.size();
        long long res = 0;
        
        priority_queue<long long>que;
        
        for(auto i: gifts)
        {
            que.push(i);
        }
        
        while(k--)
        {
            que.push(sqrt(que.top()));
            que.pop();
        }
        
        while(!que.empty())
        {
            res += que.top();
            
            que.pop();
        }
        
        return res;
    }
};