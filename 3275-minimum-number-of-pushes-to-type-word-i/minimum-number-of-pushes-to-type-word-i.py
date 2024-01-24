class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        if(n <= 8):
            return n
        elif(n <= 16):
            x = (n - 8)
            return (1 * 8) + (x * 2)
        elif(n <= 24):
            x = (n - 16)
            return (3 * 8) + (x * 3)
        else:
            x = (n - 24)
            return (6 * 8) + (x * 4)
        