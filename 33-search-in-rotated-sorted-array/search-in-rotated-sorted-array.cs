public class Solution {
    public int Search(int[] nums, int target) {
        int first = 0, last = nums.Length - 1;

        while (first <= last) {
            int mid = (first + last) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            bool leftSorted = nums[first] < nums[mid];
            bool targetLeft = nums[first] <= target && target < nums[mid];
            bool rotatedCase = nums[first] > nums[mid] && (target < nums[mid] || target >= nums[first]);

            if ((leftSorted && targetLeft) || rotatedCase) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return -1;
    }
}