class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        factor = 2

        if n == 1:
            return count
        else:
            while n > 1:
                while n % factor == 0:
                    count += factor
                    n //= factor
                factor += 1

            return count
