class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        num = ""

        while n:
            r = n % 10
            sum += r

            if r != 0:
                num += str(r)
            n //= 10

        num = num[::-1]

        return (int(num) if num else 0) * sum
