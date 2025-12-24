class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int tsum = accumulate(apple.begin(), apple.end(), 0);
        sort(capacity.begin(), capacity.end(), greater<int>());

        int count = 0;
        while (tsum > 0) {
            tsum -= capacity[count];
            count += 1;
        }

        return count;
    }
};