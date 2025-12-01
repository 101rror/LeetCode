public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        int m = batteries.Length;
        Array.Sort(batteries);
        long sum = 0;

        foreach (int x in batteries) {
            sum += x;
        }

        while (batteries[m - 1] > sum / n) {
            sum -= batteries[m - 1];
            m--;
            n--;
        }

        return sum / n;
    }
}
