class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squreSum = digitSum = 0

        while n:
            r = n % 10
            digitSum += r
            squreSum += r * r
            n //= 10

        return squreSum - digitSum >= 50
