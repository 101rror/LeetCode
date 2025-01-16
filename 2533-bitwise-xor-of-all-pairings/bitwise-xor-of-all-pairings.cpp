class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        int xor1 = 0, xor2 = 0, ans = 0;

        for (auto num1 : nums1) {
            xor1 ^= num1;
        }
        for (auto num2 : nums2) {
            xor2 ^= num2;
        }

        if (n & 1) {
            ans ^= xor2;
        }
        if (m & 1) {
            ans ^= xor1;
        }

        return ans;
    }
};