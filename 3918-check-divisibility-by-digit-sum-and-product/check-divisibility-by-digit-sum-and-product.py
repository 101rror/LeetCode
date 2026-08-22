class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum, mul = 0, 1
        nn = n

        while nn:
            rem = nn % 10
            sum += rem
            mul *= rem
            nn //= 10

        return True if n % (sum + mul) == 0 else False
