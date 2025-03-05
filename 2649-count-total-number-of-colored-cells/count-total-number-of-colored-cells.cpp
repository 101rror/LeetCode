class Solution {
public:
    long long coloredCells(int n) {
        return pow(n, 2) + pow((n - 1), 2);
    }
};