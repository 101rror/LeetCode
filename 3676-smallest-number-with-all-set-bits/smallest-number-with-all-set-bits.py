class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n.bit_length()

        return (1 << x) - 1
