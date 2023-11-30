class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        count = 0

        while(n):
            x = (n ^ (n - 1))
            count = - count - x
            n &= (n - 1)

        return abs(count)