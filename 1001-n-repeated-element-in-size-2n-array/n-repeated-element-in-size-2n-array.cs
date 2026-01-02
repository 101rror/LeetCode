public class Solution {
    public int RepeatedNTimes(int[] nums) {
        HashSet<int> seen = new HashSet<int>();

        foreach (int i in nums) {
            if (seen.Contains(i)) {
                return i;
            }
            seen.Add(i);
        }
        
        return -1;
    }
}