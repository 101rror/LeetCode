class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        rvs = b[::-1]

        while len(rvs) != 32:
            rvs += "0"

        return int(rvs, 2)
