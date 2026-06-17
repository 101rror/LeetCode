class Solution:
    def processStr(self, s: str, k: int) -> str:
        ans = 0

        for ch in s:
            if ch == "*":
                if ans:
                    ans -= 1
            elif ch == "#":
                ans *= 2
            elif ch == "%":
                continue
            else:
                ans += 1

        if ans <= k:
            return "."

        s = s[::-1]

        for ch in s:
            if ch == "*":
                ans += 1
            elif ch == "#":
                half = ans // 2
                if k >= half:
                    k -= half
                ans = half
            elif ch == "%":
                k = ans - k - 1
            else:
                if k == ans - 1:
                    return ch
                ans -= 1

        return "."
