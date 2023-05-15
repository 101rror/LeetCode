class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        n1 = len(ransomNote)
        n2 = len(magazine)
        count = 0
        n = min(n1, n2)

        for i in range(0, n):
            if(ransomNote[i] == magazine[i]):
                count += 1
        """
        s1, s2 = Counter(ransomNote), Counter(magazine)

        if ((s1 & s2) == s1):
            return True
        return False