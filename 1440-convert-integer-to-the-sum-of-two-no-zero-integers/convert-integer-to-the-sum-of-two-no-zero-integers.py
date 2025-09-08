class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            x = i
            y = n - i
            if "0" not in str(x) and "0" not in str(y):
                return [x, y]
                
        return []
