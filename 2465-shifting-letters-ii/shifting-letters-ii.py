class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        dp = [0] * (n + 1)

        for shift in shifts:
            start, end, direction = shift

            if direction == 1:
                dp[start] += 1
                dp[end + 1] -= 1
            else:
                dp[start] -= 1
                dp[end + 1] += 1

        presum = 0
        s = list(s)  

        for i in range(n):
            presum += dp[i]
            cur = ord(s[i]) - ord('a')
            new = (cur + presum % 26 + 26) % 26
            s[i] = chr(ord('a') + new)

        return ''.join(s)