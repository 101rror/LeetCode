class Solution {
public:
    int maximum69Number(int num) {
        string str = to_string(num);

        for (auto& it : str) {
            if (it == '6') {
                it = '9';
                break;
            }
        }

        return stoi(str);
    }
};