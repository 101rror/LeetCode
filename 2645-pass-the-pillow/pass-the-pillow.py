class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        r = time % (n - 1)
        q = time // (n - 1)

        if (q % 2 == 0):
            return (r + 1)
        else:
            return (n - r)

        
        