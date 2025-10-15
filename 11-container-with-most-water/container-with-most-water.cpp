#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define mpi map<int, int>
#define mps map<string, int>
#define pb push_back
#define all(x) (x).begin(), (x).end()

const int MOD = 1e9 + 7;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int left = 0, right = n - 1;
        int ans = 0;

        while (left < right) {
            int cur = min(height[left], height[right]) * (right - left);
            ans = max(ans, cur);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return ans;
    }
};