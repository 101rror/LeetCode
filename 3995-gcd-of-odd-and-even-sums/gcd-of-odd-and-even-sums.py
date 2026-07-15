from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = n * (n + 1)
        odd = n * n

        return gcd(even, odd)
