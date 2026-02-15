class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = 0, 0

        aa = a[::-1]
        bb = b[::-1]

        for i in range(len(aa)):
            x = (2**i) * int(aa[i])
            num1 += x

        for i in range(len(bb)):
            x = (2**i) * int(bb[i])
            num2 += x

        return bin(num1 + num2)[2:]
