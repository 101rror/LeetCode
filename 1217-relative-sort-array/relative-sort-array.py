class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    ans.append(arr1[j])
                    arr1[j] = -1
        
        arr1.sort()
        
        for num in arr1:
            if num != -1:
                ans.append(num)
                
        return ans