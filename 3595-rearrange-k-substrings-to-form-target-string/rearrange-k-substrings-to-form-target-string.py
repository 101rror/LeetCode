class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        x = n // k
        
        if n % k != 0:
            return False

        ss = [s[i:i + x] for i in range(0, n, x)]
        ts = [t[i:i + x] for i in range(0, n, x)]

        counter1 = Counter(ss)
        counter2 = Counter(ts)

        return counter1 == counter2