class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if(n <= 2):
            return True
            
        target = ''.join(sorted(str(n)))

        for num in range(3, 31):
            x = 1 << num
            if(''.join(sorted(str(x))) == target):
                return True

        return False