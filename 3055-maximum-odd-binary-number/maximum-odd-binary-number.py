class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = len(s)
        ze = ""
        on = ""
        ans = ""
        
        for i in range(l):
            if(s[i] == '1'):
                on += s[i]
            else:
                ze += s[i]
                
        n1 = len(on)
        n2 = len(ze)
        
        for i in range(0, n1 - 1):
            ans += on[i]
        for i in range(0, n2):
            ans += ze[i]
            
        ans += on[n1 - 1]
        
        return ans
        