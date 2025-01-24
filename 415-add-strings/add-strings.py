import sys

sys.set_int_max_str_digits(10**5)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def toint(num):
            ans = 0
            for n in num:
                ans = ans * 10 + ord(n) - ord("0")
            return ans

        ans = str(toint(num1) + toint(num2))
        return ans
