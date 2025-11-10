public class Solution {
    public int MinOperations(int[] nums) {
        var stack = new List<int>();
        int ans = 0;

        foreach (int num in nums) {
            while (stack.Count > 0 && stack[stack.Count - 1] > num) {
                stack.RemoveAt(stack.Count - 1);
            }
            if ((num != 0) && (stack.Count == 0 || stack[stack.Count - 1] < num)) {
                ans++;
                stack.Add(num);
            }
        }
        
        return ans;
    }
}