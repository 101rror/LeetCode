class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero = arr.count(0)

        for num in arr:
            if num != 0 and 2 * num in arr:
                return True
                    
        return True if zero > 1 else False