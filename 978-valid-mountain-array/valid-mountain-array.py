class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        inc, dec = 0, 0
        
        for i in range(n - 1):
            if arr[i] < arr[i + 1] and dec == 0:
                inc = 1
            elif arr[i] > arr[i + 1] and inc == 1:
                dec = 1
            else:
                return False
                
        if inc == 0 or dec == 0:
            return False
        return True
            
                
                
                