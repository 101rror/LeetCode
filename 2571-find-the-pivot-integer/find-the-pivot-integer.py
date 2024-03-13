class Solution:
    def pivotInteger(self, n: int) -> int:
        cosum = (n * (n + 1))//2

        pivot = math.sqrt(cosum)

        if (cosum % pivot == 0):
            return int(pivot)
        
        return -1