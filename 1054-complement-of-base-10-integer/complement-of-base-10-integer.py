class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit = bin(n)[2:]
        ans = ""

        for b in bit:
            if b == "0":
                ans += "1"
            else:
                ans += "0"

        return int(ans, 2)
