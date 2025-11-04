public class Solution {
    public int[] FindXSum(int[] nums, int k, int x) {
        int n = nums.Length;
        int[] ans = new int[n - k + 1];

        for (int i = 0; i <= n - k; i++) {
            Dictionary<int, int> cnt = new Dictionary<int, int>();
            for (int j = i; j < i + k; j++) {
                if (cnt.ContainsKey(nums[j])) {
                    cnt[nums[j]]++;
                }
                else {
                    cnt[nums[j]] = 1;
                }
            }

            List<int[]> freq = new List<int[]>();
            foreach (var entry in cnt) {
                freq.Add(new int[] { entry.Value, entry.Key });
            }

            freq.Sort((a, b) => b[0] != a[0] ? b[0] - a[0] : b[1] - a[1]);
            int xsum = 0;

            for (int j = 0; j < x && j < freq.Count; j++) {
                xsum += freq[j][0] * freq[j][1];
            }
            
            ans[i] = xsum;
        }

        return ans;
    }
}