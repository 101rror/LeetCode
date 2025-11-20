public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[1] != b[1] ? a[1] - b[1] : b[0] - a[0]);
        int count = 0, a = -1, b = -1;
        
        foreach (var iv in intervals) {
            int s = iv[0], e = iv[1];

            if (s > b) {
                a = e - 1;
                b = e;
                count += 2;
            } else if (s > a) {
                a = b;
                b = e;
                count++;
            }
        }

        return count;
    }
}