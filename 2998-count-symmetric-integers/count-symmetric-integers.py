class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for i in range(low, high + 1):
            a = str(i)

            if(len(a) % 2 == 0):
                b = (len(a)//2)
                c = [int(i) for i in (a[:b])]
                d = [int(i) for i in (a[b:])]
                if(len(c) == 0):
                    pass
                elif(sum(c) == sum(d)):
                    count += 1
        
        return count
                
        