public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int ans = 0;

        foreach(string value in operations) {
            if(value == "++X" || value == "X++") {
                ans++;
            }
            else {
                ans--;
            }
        }

        return ans;
    }
}