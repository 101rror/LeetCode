class Solution:
    def checkValidString(self, s: str) -> bool:
        mn, mx = 0, 0

        for c in s:
            if c == "(":
                mn, mx = mn + 1, mx + 1
            elif c == ")":
                mn, mx = mn - 1, mx - 1
            else:
                mn, mx = mn - 1, mx + 1

            if mx < 0:
                return False
            if mn < 0:
                mn = 0

        if mn == 0:
            return True