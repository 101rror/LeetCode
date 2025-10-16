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
    int compress(vector<char>& chars) {
        int n = chars.size();
        int idx = 0, i = 0;

        while (i < n) {
            char ch = chars[i];
            int count = 0;

            while (i < n && chars[i] == ch) {
                count++;
                i++;
            }

            if (count == 1) {
                chars[idx++] = ch;
            } else {
                chars[idx++] = ch;
                string str = to_string(count);

                for (auto digit : str) {
                    chars[idx++] = digit;
                }
            }
        }

        return idx;
    }
};