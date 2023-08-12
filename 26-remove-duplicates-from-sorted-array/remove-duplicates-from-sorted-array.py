class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)

        for i in range(n):
            if i != 0:
                if last != nums[i]:
                    j = j + 1
            last = nums[i]
            nums[j] = last
        j = j + 1
        nums = nums[:j]
        
        return j