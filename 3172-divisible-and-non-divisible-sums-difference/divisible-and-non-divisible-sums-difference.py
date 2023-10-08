class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        lst1 = []
        lst2 = []
        
        for i in range(n):
            if((i + 1) % m == 0):
                lst1.append(i + 1)
            else:
                lst2.append(i + 1)
                
        ans = sum(lst2) - sum(lst1)
        
        return ans

            