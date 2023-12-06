class Solution:
    def totalMoney(self, n: int) -> int:
        sum = 0
        j = 0
        k = 1

        for i in range(1, n + 1):
            if(i % 7 == 1):
                j = k
                k += 1
            else:
                j += 1
            
            sum += j

        return sum