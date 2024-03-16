class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = -1
        
        if n == 1:
            return [-1]
        
        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = mx
            mx = max(mx, temp)
            
        return arr