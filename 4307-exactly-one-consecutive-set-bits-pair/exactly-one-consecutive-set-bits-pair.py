class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0

        while n > 1:
            if (n & 3) == 3:
                count += 1
            if count > 1:
                return False
            n >>= 1
            
        return count == 1
