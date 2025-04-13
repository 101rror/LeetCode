class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = 0
        odd = 0
        mod = 10**9 + 7

        if n % 2 == 0:
            even = n // 2
            odd = n // 2
        else:
            even = (n // 2) + 1
            odd = n // 2

        ans = (pow(5, even, mod) * pow(4, odd, mod)) % mod

        return ans
