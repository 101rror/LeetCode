class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set(nums)
        i = 1

        while i in st:
            i += 1
            
        return i