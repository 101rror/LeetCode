class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(word1)
        s2 = "".join(word2)

        n1 = len(s1)
        n2 = len(s2)
        
        if(n1 != n2):
            return False

        for i in range(n1):
            if(s1[i] != s2[i]):
                return False
            else:
                continue

        return True