public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        int n = nums.Length;
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < n; i++) {
            if (nums[i][i] == '1') {
                ans.Append('0');
            }
            else {
                ans.Append('1');
            }
        }

        return ans.ToString();
    }
}