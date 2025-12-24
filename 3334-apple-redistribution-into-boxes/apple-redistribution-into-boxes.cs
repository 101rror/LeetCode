public class Solution {
    public int MinimumBoxes(int[] apple, int[] capacity) {
        int tsum = apple.Sum();
        Array.Sort(capacity);
        Array.Reverse(capacity);

        int count = 0;
        while (tsum > 0) {
            tsum -= capacity[count];
            count += 1;
        }

        return count;
    }
}