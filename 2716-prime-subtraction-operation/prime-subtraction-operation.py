class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        p = 0

        for num in nums:
            if num <= p:
                return False

            prime = num - p - 1

            while prime > 0 and not is_prime(prime):
                prime -= 1

            if prime == 0:
                p = num
            else:
                p = num - prime

        return True
