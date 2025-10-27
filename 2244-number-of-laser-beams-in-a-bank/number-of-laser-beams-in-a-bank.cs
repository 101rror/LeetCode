public class Solution {
    public int NumberOfBeams(string[] bank) {
        int ans = 0, prev = 0;

        foreach(string s in bank){
            int count = 0;
            foreach(char c in s){
                if(c == '1'){
                    count++;
                }
            }

            if(count > 0){
                ans += (prev * count);
                prev = count;
            }
        }

        return ans;
    }
}