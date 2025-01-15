class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a, b = num1.bit_count(), num2.bit_count()
        ans = num1

        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                ans ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                ans ^= 1 << i
                a += 1

        return ans
