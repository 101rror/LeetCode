class Solution:
    def processStr(self, s: str) -> str:
        ans = ""

        for ch in s:
            if ch == "*":
                if ans:
                    ans = ans[:-1]
            elif ch == "#":
                ans += ans
            elif ch == "%":
                ans = ans[::-1]
            else:
                ans += ch

        return ans
