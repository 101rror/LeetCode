class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit(x):
            pr = 1
            
            while x:
                rem = x % 10
                pr *= rem
                x //= 10
                
            return pr

        while True:
            if digit(n) % t == 0:
                return n
            
            n += 1