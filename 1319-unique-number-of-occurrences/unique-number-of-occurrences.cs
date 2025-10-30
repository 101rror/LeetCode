public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        var mp = new Dictionary<int, int> ();

        foreach (int num in arr) {
            if (mp.ContainsKey(num)) {
                mp[num]++;
            }
            else {
                mp[num] = 1;
            }
        }

        var st = new HashSet<int> (mp.Values);

        return mp.Values.Count == st.Count;
    }
}