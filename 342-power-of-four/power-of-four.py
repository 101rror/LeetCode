class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0 or n % 4 != 0:
            return False
        else:
            t = math.log(n) / math.log(4)
            if(t == int(t)):
                return True
            else:
                return False