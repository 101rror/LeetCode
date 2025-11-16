class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7
        ans, count = 0, 0

        for i in range(n):
            if s[i] == "1":
                count += 1
            else:
                ans += ((count * (count + 1)) // 2) % mod
                count = 0

        ans += ((count * (count + 1)) // 2)

        return ans
