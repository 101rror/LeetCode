class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        x, mx = 0, 0

        for i in range(1, len(b)):
            if b[i] == "1":
                mx = max(mx, i - x)
                x = i

        return mx
