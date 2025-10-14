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
    string reverseVowels(string s) {
        int n = s.length();
        string vowels = "aeiouAEIOU";
        string word = s;
        int first = 0, last = n - 1;

        while (first < last) {
            while (first < last && vowels.find(word[first]) == string::npos) {
                first++;
            }
            while (first < last && vowels.find(word[last]) == string::npos) {
                last--;
            }
            swap(word[first], word[last]);
            first++;
            last--;
        }

        return word;
    }
};