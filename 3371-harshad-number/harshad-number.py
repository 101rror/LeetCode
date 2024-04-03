class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if len(str(x)) == 1:
            return x

        xsum = 0
        num = x

        while x:
            rem = x % 10
            xsum += rem
            x //= 10

        if num % xsum == 0:
            return xsum
        
        return -1