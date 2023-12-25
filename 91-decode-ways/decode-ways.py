class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            o = int(s[i - 1])
            t = 0
            
            if(i >= 2):
                t = int(s[i - 2 : i])

            if o != 0:
                dp[i] += dp[i - 1]

            if 10 <= t <= 26:
                dp[i] += dp[i - 2]

        ans = dp[n]

        return ans