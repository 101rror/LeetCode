class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        c5, c10, c20 = 0, 0, 0

        for i in range(n):
            if(bills[i] == 5):
                c5 += 1
            elif(bills[i] == 10):
                c10 += 1
                if(c5 == 0):
                    return False
                    break
                c5 -= 1
            else:
                if(c10 >= 1 and c5 >= 1):
                    c5 -= 1
                    c10 -= 1
                elif(c5 >= 3):
                    c5 -= 3
                else:
                    return False

        return True
