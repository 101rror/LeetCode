class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        if n & 1:
            n -= 1
            
        return n + 2 - 2*self.lastRemaining(n//2)