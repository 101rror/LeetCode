public class Solution {
    public IList<string> ReadBinaryWatch(int turnedOn) {
        List<string> ans = new List<string>();

        for (int hh = 0; hh <= 11; hh++) {
            for (int mm = 0; mm <= 59; mm++) {
                if (BitCount(hh) + BitCount(mm) == turnedOn) {
                    string hour = hh.ToString();
                    string mint = (mm < 10 ? "0" : "") + mm;
                    ans.Add(hour + ":" + mint);
                }

            }
        }

        return ans;
    }

    private int BitCount(int n) {
        return Convert.ToString(n, 2).Count(c => c == '1');
    }
}