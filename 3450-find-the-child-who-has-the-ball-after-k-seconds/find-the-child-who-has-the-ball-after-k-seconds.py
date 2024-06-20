class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        posneg, j = 1, 0

        for i in range(k):
            j += posneg
            if j == 0 or j == n - 1:
                posneg *= -1
                
        return j