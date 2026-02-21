class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        while left <= right:
            one = bin(left).count("1")

            if one in primes:
                count += 1

            left += 1

        return count
