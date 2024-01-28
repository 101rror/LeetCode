class Solution:
    def countKeyChanges(self, s: str) -> int:
        x = s.lower()
        count = 0
        
        for i in range(len(s) - 1):
            if x[i] != x[i + 1]:
                count += 1
                                        
        return count