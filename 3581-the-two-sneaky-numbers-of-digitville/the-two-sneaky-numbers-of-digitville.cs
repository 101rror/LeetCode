public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        List<int> ans = new List<int>();

        foreach (int num in nums) {
            if (!seen.Contains(num)) {
                seen.Add(num);
            }
            else {
                ans.Add(num);
            }
        }

        return ans.ToArray();
    }
}