class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        count = 0

        while left <= right:
            one = bin(left).count("1")

            if isPrime(one):
                count += 1

            left += 1

        return count
