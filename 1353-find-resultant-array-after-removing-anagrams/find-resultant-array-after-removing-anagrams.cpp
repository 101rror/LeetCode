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
    vector<string> removeAnagrams(vector<string>& words) {
        vs ans;
        string prev = "";

        for (auto& word : words) {
            string srt = word;
            sort(all(srt));

            if (srt != prev) {
                ans.pb(word);
            }
            prev = srt;
        }

        return ans;
    }
};