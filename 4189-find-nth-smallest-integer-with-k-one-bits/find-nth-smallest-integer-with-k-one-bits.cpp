class Solution {
public:
    long long nthSmallest(long long rank, int setBitsCount) {
        const int mx = 60;
        long long comb[mx][mx] = {0};

        for (int i = 0; i < mx; i++) {
            comb[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        long long ans = 0;
        long long rem = rank - 1;

        for (int left = setBitsCount; left > 0; --left) {
            int pos = 0;

            while (pos + 1 < mx && comb[pos + 1][left] <= rem) {
                pos++;
            }

            ans |= (1LL << pos);
            rem -= comb[pos][left];
        }

        return ans;
    }
};
