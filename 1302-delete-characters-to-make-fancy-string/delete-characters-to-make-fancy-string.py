class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        freq = 1
        prev = s[0]

        if len(s) < 3:
            return s
        
        for i in range(1, len(s)):
            if s[i] == prev:
                freq += 1
            else:
                prev = s[i]
                freq = 1

            if freq < 3:
                ans += s[i]

        return ans