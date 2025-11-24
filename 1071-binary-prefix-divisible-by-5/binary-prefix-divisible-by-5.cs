public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        var ans = new List<bool>();
        int x = 0;

        foreach (int num in nums) {
            x = (x * 2 + num) % 5;
            ans.Add(x == 0);
        }

        return ans;
    }
}