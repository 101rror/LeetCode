class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n):
            if s[i - 1] == "0" and s[i] == "1":
                return False

        return True
