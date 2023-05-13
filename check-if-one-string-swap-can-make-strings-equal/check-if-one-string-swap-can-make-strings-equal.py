class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool: 
        length = len(s1) 
        count = 0

        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        if sorted(s1) != sorted(s2):
            return False

        for  i in range(length):
            if s1[i] != s2[i]:
                count += 1

        if count == 2:
            return True
        else: False
        