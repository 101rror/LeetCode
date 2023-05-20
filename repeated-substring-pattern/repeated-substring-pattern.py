class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n//2 + 1):   
            if s == s[:i] * (n // i):
                return True

        return False
