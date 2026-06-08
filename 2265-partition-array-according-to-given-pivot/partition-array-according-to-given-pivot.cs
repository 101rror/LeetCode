public class Solution {
    public int[] PivotArray(int[] nums, int pivot) {
        List<int> less = new();
        List<int> equal = new();
        List<int> greater = new();

        foreach (int num in nums) {
            if (num < pivot) {
                less.Add(num);
            }
            else if (num == pivot) {
                equal.Add(num);
            }
            else {
                greater.Add(num);
            }
        }

        return less.Concat(equal).Concat(greater).ToArray();
    }
}