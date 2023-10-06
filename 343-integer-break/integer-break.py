class Solution:
    def integerBreak(self, n: int) -> int:
        ans = []

        if(n == 2 or n == 3):
            return (n - 1)

        while(n):
            if(not n % 3):
                n -= 3
                ans.append(3)
            else:
                n -= 2
                ans.append(2)

        res = 1
        
        for num in ans:
            res *= num

        return res