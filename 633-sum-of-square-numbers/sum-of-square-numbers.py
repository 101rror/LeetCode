class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first = 0
        last = int(sqrt(c))

        while (first <= last):
            cur = (first * first + last * last)

            if (cur == c):
                return True
            if (cur < c):
                first += 1
            else:
                last -= 1
                
        return False