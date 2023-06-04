class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s = sorted(s)
        n = len(s)
        count = 1
        
        for i in range(0, n - 1):
            if(s[i] != s[i + 1]):
                count += 1
                
        return count
        