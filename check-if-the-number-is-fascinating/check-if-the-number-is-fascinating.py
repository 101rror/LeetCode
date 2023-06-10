class Solution:
    def isFascinating(self, n: int) -> bool:
        n1 = (2 * n)
        n2 = (3 * n)
        
        x1 = str(n)
        x2 = str(n1)
        x3 = str(n2)
        x = x1 + x2 + x3
        
        x = sorted(x)
        ln = len(x)
        
        for i in range(0, ln - 1):
            if(x[i] == x[i + 1] or x[i] == '0'):
                return False
        return True
        