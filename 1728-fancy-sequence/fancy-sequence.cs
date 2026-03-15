public class Fancy {

    const long MOD = 1_000_000_007;
    List<long> lst = new List<long>();

    long mul = 1;
    long add = 0;

    public Fancy() {}

    public void Append(int val) {
        long normalized = (val - add + MOD) % MOD;
        normalized = normalized * ModInverse(mul) % MOD;
        lst.Add(normalized);
    }

    public void AddAll(int inc) {
        add = (add + inc) % MOD;
    }

    public void MultAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }

    public int GetIndex(int idx) {
        if(idx >= lst.Count) return -1;

        long val = (lst[idx] * mul + add) % MOD;
        return (int)val;
    }

    private long ModInverse(long x) {
        return Pow(x, MOD - 2);
    }

    private long Pow(long x, long y) {
        long res = 1;
        x %= MOD;

        while(y > 0) {
            if((y & 1) == 1)
                res = (res * x) % MOD;

            x = (x * x) % MOD;
            y >>= 1;
        }

        return res;
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * int param_4 = obj.GetIndex(idx);
 */