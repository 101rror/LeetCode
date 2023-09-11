class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target = sorted(target)
        arr = sorted(arr)

        if(target == arr):
            return True
        return False
        