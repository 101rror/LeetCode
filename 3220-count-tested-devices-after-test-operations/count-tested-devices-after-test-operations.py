class Solution:
    def countTestedDevices(self, lst: List[int]) -> int:
        def de(x, arr):
            for i in range(x, len(arr)):
                arr[i] -= 1
                if(arr[i] < 0):
                    arr[i] = 0
                else:
                    continue
                
            return arr
        
        n = len(lst)
        count = 0
        i = 0
        
        for i in range(n):
            if (lst[i] > 0):
                lst = de(i + 1, lst)
                count += 1
                 
        return count          