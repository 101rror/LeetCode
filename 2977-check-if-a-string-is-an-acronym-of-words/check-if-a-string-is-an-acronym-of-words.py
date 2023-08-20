class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n = len(words)
        n1 = len(s)
        
        if(n != n1):
            return False
        
        for i in range(n):
            x = words[i]
            c = x[0]
            
            if(c != s[i]):
                return False
        return True