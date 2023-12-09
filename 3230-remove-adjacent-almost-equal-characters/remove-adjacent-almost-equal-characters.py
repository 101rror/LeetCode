class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        count = 0
        i = 0
        
        while(i < n - 1):
            x = ord(word[i])
            y = ord(word[i + 1])
            t = abs(x - y)
            
            if(t == 1 or t == 0):
                count += 1
                i += 2
            else:
                i += 1
                
        return count