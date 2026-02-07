class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)

        if s.count("a") == 0:
            return True

        for i in range(1, n):
            if s[i - 1] == "b" and s[i] == "a":
                return False

        return True
