class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ans = n
        dp = [0, 0]

        for i in range(n):
            dp[(ord(s[i]) ^ i) & 1] += 1

        for i in range(n):
            c = ord(s[i])
            dp[(c ^ i) & 1] -= 1
            dp[(c ^ (n + i)) & 1] += 1
            ans = min(ans, min(dp))

        return ans
