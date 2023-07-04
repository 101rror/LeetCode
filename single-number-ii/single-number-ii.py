class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = list(set(nums))

        for i in s:
            if(nums.count(i) == 1):
                return i