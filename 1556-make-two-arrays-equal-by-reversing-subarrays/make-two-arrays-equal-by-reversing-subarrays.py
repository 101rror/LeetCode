class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        sumtarget = 0
        sumarr = 0

        for i in target:
            sumtarget += (i * i)
        for i in arr:
            sumarr += (i * i)

        return True if sumtarget == sumarr and sum(arr) == sum(target) else False 