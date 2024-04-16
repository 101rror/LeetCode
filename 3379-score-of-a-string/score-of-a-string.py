class Solution:
    def scoreOfString(self, s: str) -> int:
        tsum = 0

        for i in range(1, len(s)):
            tsum += abs(ord(s[i - 1]) - ord(s[i]))

        return tsum