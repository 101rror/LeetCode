class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        count = 1

        for i in range(1, n):
            if s[i] == ans[-1]:
                count += 1
                if count < 3:
                    ans += s[i]
            else:
                count = 1
                ans += s[i]
                
        return ans