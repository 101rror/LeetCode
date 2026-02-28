class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        str = ""

        for i in range(1, n + 1):
            b = bin(i)[2:]
            str += b

        return int(str, 2) % mod
