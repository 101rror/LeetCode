class Solution:
    def largestGoodInteger(self, s: str) -> str:
        ans = ""
        n = len(s)

        for i in range(n - 2):
            if(s[i] ==  s[i + 1] and s[i + 1] == s[i + 2]):
                ans += s[i] + s[i + 1] + s[i + 2]

        res = ''.join(sorted(ans, reverse=True))

        st = ""
        t = 0

        for i in res:
            st += i
            t += 1
            if(t == 3):
                break

        return st
